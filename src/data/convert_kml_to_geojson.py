import json
import xml.etree.ElementTree as ET
from pathlib import Path


def kml_to_geojson(kml_path: Path, out_path: Path) -> None:
    """
    Convierte un KML sencillo (como los de este proyecto) a un GeoJSON muy básico.
    Extrae solo el <name> y <description> del <Document>.
    """

    text = kml_path.read_text(encoding="utf-8")

    # Namespace de KML
    ns = {"kml": "http://www.opengis.net/kml/2.2"}

    root = ET.fromstring(text)
    doc = root.find("kml:Document", ns)

    name_el = doc.find("kml:name", ns) if doc is not None else None
    desc_el = doc.find("kml:description", ns) if doc is not None else None

    name = name_el.text if name_el is not None else ""
    description = desc_el.text if desc_el is not None else ""

    feature = {
        "type": "Feature",
        "geometry": None,  # por ahora sin geometría (nuestros KML de plantilla no tienen)
        "properties": {
            "name": name,
            "description": description,
            "source_file": kml_path.name,
        },
    }

    feature_collection = {
        "type": "FeatureCollection",
        "features": [feature],
    }

    out_path.write_text(
        json.dumps(feature_collection, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"✅ Convertido: {kml_path.name} -> {out_path.name}")


def main() -> None:
    # Detectar la raíz del proyecto a partir de la ubicación de este archivo
    # src/data/ -> src -> raíz del proyecto
    base_dir = Path(__file__).resolve().parents[2]

    raw_dir = base_dir / "data" / "raw"
    interim_dir = base_dir / "data" / "interim"

    interim_dir.mkdir(parents=True, exist_ok=True)

    kml_files = list(raw_dir.glob("*.kml"))

    if not kml_files:
        print(f"⚠️ No se encontraron archivos .kml en: {raw_dir}")
        return

    for kml_file in kml_files:
        out_file = interim_dir / (kml_file.stem + ".geojson")
        kml_to_geojson(kml_file, out_file)


if __name__ == "__main__":
    main()
