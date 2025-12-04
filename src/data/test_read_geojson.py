import geopandas as gpd
import os

INTERIM_FOLDER = "data/interim"

files = [
    "climatologia_extrema_1902_2011.geojson",
    "temperatura_maxima_promedio_1902_2011.geojson",
    "temperatura_media_1902_2011.geojson",
    "temperatura_minima_promedio_1902_2011.geojson"
]

print("\n=== VALIDANDO GEOJSON ===\n")

for f in files:
    path = os.path.join(INTERIM_FOLDER, f)
    print(f"Probando: {path}")

    try:
        gdf = gpd.read_file(path)
        print(f"➤ OK: {f} leído correctamente")
        print(f"  Filas: {len(gdf)}  |  Columnas: {list(gdf.columns)}\n")
    except Exception as e:
        print(f"❌ ERROR al leer {f}")
        print("Detalle:", e, "\n")

print("=== FIN ===")
