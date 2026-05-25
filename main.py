# Punto de entrada del pipeline de Data Science.
# Orquesta dos flujos independientes — usuarios y comercios — siguiendo
# las cuatro capas del proyecto: api → processing → transforming → visualization.

# ---------------------------------------------------------------------------
# Flujo USUARIOS
# ---------------------------------------------------------------------------
from src.api.usuarios_consumo_api import obtener_usuarios
from src.processing.usuarios_limpieza import limpiar_usuarios
from src.transforming.usuarios_transformacion import transformacion_datos_usuarios
from src.visualization.usuarios_graficos import (
    graficar_usuarios_por_rol,
    graficar_usuarios_por_tipo_documento,
    graficar_adultos_mayores_por_rol,
    graficar_edad_promedio_por_rol,
    graficar_jovenes_por_tipo_documento,
)

# ---------------------------------------------------------------------------
# Flujo COMERCIOS
# ---------------------------------------------------------------------------
from src.api.comercios_consumo_api import obtener_comercios
from src.processing.comercios_limpieza import limpiar_comercios
from src.transforming.comercios_transformacion import transformacion_datos_comercios
from src.visualization.comercios_graficos import (
    graficar_comercios_por_actividad,
    graficar_comercios_por_direccion,
    graficar_presencia_web,
    graficar_top_representantes,
    graficar_comercios_por_rango_nit,
)


# ===========================================================================
# Pipeline USUARIOS
# ===========================================================================
# 1. Consumir el API y traer los usuarios como DataFrame.
dataframe_usuarios = obtener_usuarios()
# 2. Limpiar/normalizar columnas y descartar filas inválidas.
dataframe_usuarios_limpio = limpiar_usuarios(dataframe_usuarios)
# 3. Aplicar las cinco agregaciones de negocio.
resultados_usuarios = transformacion_datos_usuarios(dataframe_usuarios_limpio)
# 4. Renderizar y guardar los PNGs de cada agregación.
graficar_usuarios_por_rol(resultados_usuarios["usuarios_por_rol"])
graficar_usuarios_por_tipo_documento(resultados_usuarios["usuarios_por_tipo_documento"])
graficar_adultos_mayores_por_rol(resultados_usuarios["adultos_mayores_por_rol"])
graficar_edad_promedio_por_rol(resultados_usuarios["edad_promedio_por_rol"])
graficar_jovenes_por_tipo_documento(resultados_usuarios["jovenes_por_tipo_documento"])


# ===========================================================================
# Pipeline COMERCIOS
# ===========================================================================
# 1. Consumir el API y traer los comercios como DataFrame.
dataframe_comercios = obtener_comercios()
# 2. Limpiar/normalizar columnas y descartar filas inválidas.
dataframe_comercios_limpio = limpiar_comercios(dataframe_comercios)
# 3. Aplicar las cinco agregaciones de negocio para comercios.
resultados_comercios = transformacion_datos_comercios(dataframe_comercios_limpio)
# 4. Renderizar y guardar los PNGs de cada agregación.
graficar_comercios_por_actividad(resultados_comercios["comercios_por_actividad"])
graficar_comercios_por_direccion(resultados_comercios["comercios_por_direccion"])
graficar_presencia_web(resultados_comercios["presencia_web"])
graficar_top_representantes(resultados_comercios["top_representantes"])
graficar_comercios_por_rango_nit(resultados_comercios["comercios_por_rango_nit"])
