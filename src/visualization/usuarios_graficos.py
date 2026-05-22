import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

GRAFICOS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "frontend" / "src" / "assets" / "python" / "graficos"
GRAFICOS_DIR.mkdir(parents=True, exist_ok=True)

def graficar_usuarios_por_rol(dataframe_limpio):
    plt.figure(figsize=(7, 7))
    plt.pie(
        dataframe_limpio["cantidad"],
        labels=dataframe_limpio["rol"],
        autopct="%1.1f%%",
        colors=sns.color_palette("Set2", len(dataframe_limpio)),
        startangle=90
    )
    plt.title("Cantidad de Usuarios Registrados por Rol")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "usuarios_por_rol.png", dpi=150)
    plt.show()


def graficar_usuarios_por_tipo_documento(dataframe_limpio):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=dataframe_limpio, x="tipoDocumento", y="cantidad", palette="Blues")
    plt.title("Distribución de usuarios por tipo de documento")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "usuarios_por_tipo_documento.png", dpi=150)
    plt.show()

def graficar_adultos_mayores_por_rol(dataframe_limpio):
    plt.figure(figsize=(7, 7))
    plt.pie(
        dataframe_limpio["cantidad"],
        labels=dataframe_limpio["rol"],
        autopct="%1.1f%%",
        colors=sns.color_palette("Oranges", len(dataframe_limpio)),
        startangle=90
    )
    plt.title("Adultos mayores (≥60 años) por rol")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "adultos_mayores_por_rol.png", dpi=150)
    plt.show()

def graficar_edad_promedio_por_rol(dataframe_limpio):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=dataframe_limpio, x="rol", y="edad_promedio", palette="muted")
    plt.title("Edad promedio por rol")
    plt.ylabel("Edad promedio (años)")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "edad_promedio_por_rol.png", dpi=150)
    plt.show()

def graficar_jovenes_por_tipo_documento(dataframe_limpio):
    plt.figure(figsize=(7, 7))
    plt.pie(
        dataframe_limpio["cantidad"],
        labels=dataframe_limpio["tipoDocumento"],
        autopct="%1.1f%%",
        colors=sns.color_palette("Set1", len(dataframe_limpio)),
        startangle=90
    )
    plt.title("Usuarios jóvenes (18–30 años) por tipo de documento")
    plt.tight_layout()
    plt.savefig(GRAFICOS_DIR / "jovenes_por_tipo_documento.png", dpi=150)
    plt.show()
