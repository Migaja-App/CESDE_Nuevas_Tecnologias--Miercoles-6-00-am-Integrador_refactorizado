from src.api.usuarios_consumo_api import obtener_usuarios
from src.processing.usuarios_limpieza import limpiar_usuarios
from src.transforming.usuarios_transformacion import transformacion_datos_usuarios
from src.visualization.usuarios_graficos import (
    graficar_usuarios_por_rol,
    graficar_usuarios_por_tipo_documento,
    graficar_adultos_mayores_por_rol,
    graficar_edad_promedio_por_rol,
    graficar_jovenes_por_tipo_documento
)

dataframe_usuarios = obtener_usuarios()
dataframe_limpio = limpiar_usuarios(dataframe_usuarios)
resultados_transformacion = transformacion_datos_usuarios(dataframe_limpio)

# Generar gráficos
graficar_usuarios_por_rol(resultados_transformacion["usuarios_por_rol"])
graficar_usuarios_por_tipo_documento(resultados_transformacion["usuarios_por_tipo_documento"])
graficar_adultos_mayores_por_rol(resultados_transformacion["adultos_mayores_por_rol"])
graficar_edad_promedio_por_rol(resultados_transformacion["edad_promedio_por_rol"])
graficar_jovenes_por_tipo_documento(resultados_transformacion["jovenes_por_tipo_documento"])

