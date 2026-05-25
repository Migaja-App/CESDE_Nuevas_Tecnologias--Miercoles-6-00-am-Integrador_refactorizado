import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Este módulo se encarga de renderizar los gráficos a partir de los
# DataFrames producidos por la capa de transformación. Cada gráfico se
# guarda como PNG en la carpeta de assets del frontend para que la app
# React pueda mostrarlos sin volver a ejecutar el pipeline Python.

# Ruta destino de los PNGs. Se calcula relativa a la ubicación del
# archivo actual subiendo cuatro niveles hasta la raíz del workspace
# y entrando luego a frontend/src/assets/python/graficos.
GRAFICOS_DIR = (
    Path(__file__).resolve().parent.parent.parent.parent
    / "frontend" / "src" / "assets" / "python" / "graficos" / "comercios"
)
# mkdir con parents=True crea toda la cadena de carpetas si no existe,
# y exist_ok=True evita error cuando ya existe.
GRAFICOS_DIR.mkdir(parents=True, exist_ok=True)


def graficar_comercios_por_actividad(dataframe_limpio):
    # Gráfico de barras horizontales: las actividades pueden ser textos
    # largos, así que horizontal mejora la legibilidad de las etiquetas.
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=dataframe_limpio,
        y="actividad",
        x="cantidad",
        palette="Set2",
    )
    plt.title("Cantidad de Comercios por Actividad Económica")
    plt.xlabel("Cantidad de comercios")
    plt.ylabel("Actividad")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "comercios_por_actividad.png", dpi=150)
    plt.show()


def graficar_comercios_por_direccion(dataframe_limpio):
    # Gráfico de barras vertical para distribución por dirección/zona.
    # Se rota el eje X 45° porque las direcciones son cadenas largas.
    plt.figure(figsize=(9, 5))
    sns.barplot(
        data=dataframe_limpio,
        x="direccion",
        y="cantidad",
        palette="Blues",
    )
    plt.title("Distribución de comercios por dirección")
    plt.xlabel("Dirección")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "comercios_por_direccion.png", dpi=150)
    plt.show()


def graficar_presencia_web(dataframe_limpio):
    # Pie chart con la proporción de comercios que tienen sitio web
    # versus los que no. Visual sencillo para una métrica binaria.
    plt.figure(figsize=(7, 7))
    plt.pie(
        dataframe_limpio["cantidad"],
        labels=dataframe_limpio["tiene_sitio_web"],
        autopct="%1.1f%%",
        colors=sns.color_palette("pastel", len(dataframe_limpio)),
        startangle=90,
    )
    plt.title("Comercios con vs sin sitio web")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "presencia_web.png", dpi=150)
    plt.show()


def graficar_top_representantes(dataframe_limpio):
    # Top N representantes legales con más comercios. Se usa barra
    # horizontal porque los nombres son cadenas potencialmente largas.
    plt.figure(figsize=(10, 6))
    sns.barplot(
        data=dataframe_limpio,
        y="representanteLegal",
        x="cantidad",
        palette="Oranges_r",
    )
    plt.title("Top 10 representantes legales por cantidad de comercios")
    plt.xlabel("Cantidad de comercios")
    plt.ylabel("Representante legal")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "top_representantes.png", dpi=150)
    plt.show()


def graficar_comercios_por_rango_nit(dataframe_limpio):
    # Distribución de comercios por rango de NIT (bucketizado en 3 partes).
    # Útil para ver si la base de NIT está concentrada o dispersa.
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=dataframe_limpio,
        x="rango_nit",
        y="cantidad",
        palette="muted",
    )
    plt.title("Comercios por rango de NIT")
    plt.xlabel("Rango de NIT")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "comercios_por_rango_nit.png", dpi=150)
    plt.show()
