import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# CONFIGURACIÓN DE RUTAS
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PROCESSED = BASE_DIR / "data" / "processed" / "temperaturas_mx_1902_2011.csv"
FIGURES_DIR = BASE_DIR / "reports" / "figures"

# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():
    print("Cargando datos procesados...")
    print(f"Ruta esperada del CSV: {DATA_PROCESSED}")

    if not DATA_PROCESSED.exists():
        print("\nERROR: No se encontró el archivo de datos procesados.")
        print(f"Verifica que exista:\n    {DATA_PROCESSED}")
        return

    df = pd.read_csv(DATA_PROCESSED)
    print("Columnas:", df.columns.tolist())
    print(df.head(), "\n")

    # Crear carpeta de figuras si no existe
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # =======================================================
    # 1. Promedio de temperatura media por región
    # =======================================================
    print("Generando gráfico: temperatura media por región...")

    mean_by_region = (
        df.groupby("region_name")["tmean_c"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))
    mean_by_region.plot(kind="bar", color="skyblue", edgecolor="black")
    plt.title("Temperatura media promedio por región (1902–2011)")
    plt.ylabel("°C")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "tmean_promedio_por_region.png")
    plt.close()

    print("✔ Gráfico guardado: tmean_promedio_por_region.png\n")

    # =======================================================
    # 2. Tendencia histórica de temperatura media
    # =======================================================
    print("Generando gráfico: tendencia de temperatura media...")

    trend = (
        df.groupby("year")["tmean_c"]
        .mean()
    )

    plt.figure(figsize=(8, 5))
    plt.plot(trend.index, trend.values, marker="o")
    plt.title("Tendencia histórica de temperatura media en México (1902–2011)")
    plt.xlabel("Año")
    plt.ylabel("Temperatura media (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "tendencia_tmean.png")
    plt.close()

    print("✔ Gráfico guardado: tendencia_tmean.png\n")

    # =======================================================
    # 3. Comparación de amplitud térmica por región
    # =======================================================
    print("Generando gráfico: amplitud térmica por región...")

    df["amplitud_termica"] = df["tmax_c"] - df["tmin_c"]

    amplitud = (
        df.groupby("region_name")["amplitud_termica"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))
    amplitud.plot(kind="bar", color="salmon", edgecolor="black")
    plt.title("Amplitud térmica promedio por región")
    plt.ylabel("°C")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "amplitud_termica_por_region.png")
    plt.close()

    print("✔ Gráfico guardado: amplitud_termica_por_region.png\n")

    print("✔✔ Todos los gráficos fueron generados correctamente.")
    print(f"Carpeta de salida:\n{FIGURES_DIR}")


# ============================================================
# EJECUCIÓN DIRECTA
# ============================================================

if __name__ == "__main__":
    main()
