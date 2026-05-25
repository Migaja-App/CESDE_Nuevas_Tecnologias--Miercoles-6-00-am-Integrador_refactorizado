import pandas as pd

# Este módulo aplica las transformaciones/agregaciones de negocio sobre
# el DataFrame de comercios ya limpio. Devuelve un diccionario con cinco
# DataFrames resultado, cada uno listo para ser graficado.


def transformacion_datos_comercios(dataframe_limpio):

    # Filtro 1 — Cantidad de comercios por tipo de actividad económica.
    # Equivalente, en el flujo de usuarios, al "agrupamiento por rol".
    # Permite ver qué actividades concentran más comercios en la plataforma.
    comercios_por_actividad = (
        dataframe_limpio
        .groupby("actividad")["id"]
        .count()
        .reset_index(name="cantidad")
        .sort_values("cantidad", ascending=False)
    )

    # Filtro 2 — Distribución de comercios por dirección/zona.
    # Da una idea de la concentración geográfica de los comercios
    # registrados (en el seed son 5 direcciones fijas; en producción
    # podrían ser más variadas).
    comercios_por_direccion = (
        dataframe_limpio
        .groupby("direccion")["id"]
        .count()
        .reset_index(name="cantidad")
        .sort_values("cantidad", ascending=False)
    )

    # Filtro 3 — Comercios con sitio web vs sin sitio web.
    # Aprovecha que "sitioWeb" es el único campo nullable del modelo.
    # Es un indicador de madurez digital del comercio.
    # Se considera "sin web" cuando el valor es nulo o cadena vacía.
    sitio_web_serie = dataframe_limpio["sitioWeb"]
    tiene_web = sitio_web_serie.notna() & (sitio_web_serie.str.len() > 0)
    presencia_web = pd.DataFrame({
        "tiene_sitio_web": ["con sitio web", "sin sitio web"],
        "cantidad": [int(tiene_web.sum()), int((~tiene_web).sum())],
    })

    # Filtro 4 — Top 10 representantes legales con más comercios a cargo.
    # Útil para detectar concentración de control (un mismo representante
    # legal asociado a múltiples comercios distintos).
    top_representantes = (
        dataframe_limpio
        .groupby("representanteLegal")["id"]
        .count()
        .reset_index(name="cantidad")
        .sort_values("cantidad", ascending=False)
        .head(10)
    )

    # Filtro 5 — Comercios por rango de NIT.
    # El seed asigna NITs en el rango [900000000, 900000099]. Se bucketiza
    # en 3 segmentos para visualizar la distribución. Si en producción el
    # rango cambia, los buckets se ajustan dinámicamente con pd.cut
    # usando 3 intervalos de igual amplitud sobre min/max observados.
    nit_min = dataframe_limpio["nit"].min()
    nit_max = dataframe_limpio["nit"].max()
    # pd.cut divide [nit_min, nit_max] en 3 intervalos de igual amplitud.
    # include_lowest=True garantiza que el valor mínimo entre en el primer bucket.
    rangos_nit = pd.cut(
        dataframe_limpio["nit"],
        bins=3,
        include_lowest=True,
    )
    comercios_por_rango_nit = (
        dataframe_limpio
        .assign(rango_nit=rangos_nit.astype(str))
        .groupby("rango_nit")["id"]
        .count()
        .reset_index(name="cantidad")
    )

    # Se empaqueta todo en un diccionario para que la capa de visualización
    # consuma los resultados por nombre semántico, no por posición.
    resultados = {
        "comercios_por_actividad": comercios_por_actividad,
        "comercios_por_direccion": comercios_por_direccion,
        "presencia_web": presencia_web,
        "top_representantes": top_representantes,
        "comercios_por_rango_nit": comercios_por_rango_nit,
    }

    return resultados
