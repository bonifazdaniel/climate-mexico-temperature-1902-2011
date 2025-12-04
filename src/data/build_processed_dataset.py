import geopandas as gpd
import pandas as pd
from pathlib import Path


def get_base_dir() -> Path:
    # src/data/build_processed_dataset.py -> proyecto (2 niveles arriba)
    return Path(__file__).resolve().parents[2]


def build_processed_dataset():
    base_dir = get_base_dir()
    interim_dir = base_dir / "data" / "interim"
    processed_dir = base_dir / "data" / "processed"
    processed_dir.mkdir(parents=True, exist_ok=True)

    output_file = processed_dir / "temperaturas_mx_1902_2011.csv"

    # Archivos que esperamos encontrar en data/interim
    expected_files = [
        "climatologia_extrema_1902_2011.geojson",
        "temperatura_maxima_promedio_1902_2011.geojson",
        "temperatura_media_1902_2011.geojson",
        "temperatura_minima_promedio_1902_2011.geojson",
    ]

    records = []

    for filename in expected_files:
        path = interim_dir / filename
        if not path.exists():
            print(f"[ADVERTENCIA] No se encontró {path}, se omite.")
            continue

        print(f"Leyendo {path} ...")
        gdf = gpd.read_file(path)

        # Intentar identificar una columna de ID razonable
        id_col = None
        for candidate in gdf.columns:
            cl = str(candidate).lower()
            if cl in ("id", "gid", "objectid", "id_obj", "id_1"):
                id_col = candidate
                break

        if id_col is None:
            # Si no hay ID claro, creamos uno basado en el índice
            id_col = "feature_id"
            gdf[id_col] = gdf.index.astype(int)

        # Centroides (lat/lon) para poder mapear sin la geometría
        if "geometry" in gdf.columns and gdf.geometry.notna().any():
            centroids = gdf.geometry.centroid
            gdf["lon"] = centroids.x
            gdf["lat"] = centroids.y
        else:
            gdf["lon"] = None
            gdf["lat"] = None

        # Columnas de valor: todas las que no sean geometry, lat, lon, id_col
        exclude = {id_col, "geometry", "lat", "lon"}
        value_cols = [c for c in gdf.columns if c not in exclude]

        if not value_cols:
            print(f"[ADVERTENCIA] {path} no tiene columnas de datos además de la geometría/ID.")
            continue

        # Convertimos a formato largo: una fila por (feature, columna de valor)
        for vcol in value_cols:
            sub = gdf[[id_col, "lat", "lon", vcol]].copy()
            sub = sub.rename(
                columns={
                    id_col: "feature_id",
                    vcol: "value",
                }
            )
            sub["source_file"] = filename
            sub["variable"] = vcol
            records.append(sub)

    if not records:
        raise RuntimeError("No se generaron registros; revisa los GeoJSON en data/interim.")

    df_final = pd.concat(records, ignore_index=True)

    # Ordenamos columnas para mayor claridad
    cols_order = ["source_file", "variable", "feature_id", "lat", "lon", "value"]
    df_final = df_final[cols_order]

    print(f"Guardando dataset procesado en {output_file} ...")
    df_final.to_csv(output_file, index=False)
    print("Listo. Filas generadas:", len(df_final))


if __name__ == "__main__":
    build_processed_dataset()
