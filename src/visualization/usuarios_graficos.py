import matplotlib.pyplot as plt
import seaborn as sns

def graficar_usuarios_por_rol(dataframe_limpio):
    plt.figure(figsize=(10, 6))
    sns.barplot(data = dataframe_limpio, x="rol", y="cantidad", palette="Set2")
    plt.title("Cantidad de Usuarios Registrados por Rol")
    plt.tight_layout()
    plt.show()


def graficar_usuarios_por_tipo_documento(dataframe_limpio):
    plt.figure(figsize=(8, 5))
    sns.barplot(data = dataframe_limpio, x="tipoDocumento", y="cantidad", palette="Blues")
    plt.title("Distribución de usuarios por tipo de documento")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def graficar_adultos_mayores_por_rol(dataframe_limpio):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=dataframe_limpio, x="rol", y="cantidad", palette="Oranges")
    plt.title("Adultos mayores (≥60 años) por rol")
    plt.tight_layout()
    plt.show()

def graficar_edad_promedio_por_rol(dataframe_limpio):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=dataframe_limpio, x="rol", y="edad_promedio", palette="muted")
    plt.title("Edad promedio por rol")
    plt.ylabel("Edad promedio (años)")
    plt.tight_layout()
    plt.show()

def graficar_jovenes_por_tipo_documento(dataframe_limpio):
    plt.figure(figsize=(8, 5))
    sns.barplot(data=dataframe_limpio, x="tipoDocumento", y="cantidad", palette="Set1")
    plt.title("Usuarios jóvenes (18–30 años) por tipo de documento")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()