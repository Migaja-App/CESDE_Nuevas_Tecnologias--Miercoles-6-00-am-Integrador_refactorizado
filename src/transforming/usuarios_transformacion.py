import pandas as pd

def transformacion_datos_usuarios(dataframe_limpio):

    # filtro 1 - Cantidad de usuarios registrados por rol
    agrupacion_por_rol = (
        dataframe_limpio
        .groupby("rol")["id"]
        .count()
        .reset_index(name="cantidad")
    )

    # filtro 2 - distribucion de usuarios por tipo de documento
    agrupacion_por_tipo_documento = (
        dataframe_limpio
        .groupby("tipoDocumento")["id"]
        .count()
        .reset_index(name="cantidad")
    )

    # filtro 3 - edad promedio de los usuarios por rol
    filtro_adultos_mayores = dataframe_limpio.query("edad >= 60")
    adultos_mayores_por_rol = (
        filtro_adultos_mayores
        .groupby("rol")["id"]
        .count()
        .reset_index(name="cantidad")
    )

    # filtro 4  - edad promedio por rol
    edad_promedio_por_rol = (
        dataframe_limpio
        .groupby("rol")["edad"]
        .mean()
        .reset_index(name="edad_promedio")
    )

    # filtro 5 - usuarios jovenes (18 - 30 años) por tipo de documento
    filtro_jovenes = dataframe_limpio.query("edad >= 18 and edad <= 30")
    jovenes_por_tipo_documento = (
        filtro_jovenes
        .groupby("tipoDocumento")["id"]
        .count()
        .reset_index(name="cantidad")
    ) 

    resultados = {
        "usuarios_por_rol": agrupacion_por_rol,
        "usuarios_por_tipo_documento": agrupacion_por_tipo_documento,
        "adultos_mayores_por_rol": adultos_mayores_por_rol,
        "edad_promedio_por_rol": edad_promedio_por_rol,
        "jovenes_por_tipo_documento": jovenes_por_tipo_documento
    }

    return resultados