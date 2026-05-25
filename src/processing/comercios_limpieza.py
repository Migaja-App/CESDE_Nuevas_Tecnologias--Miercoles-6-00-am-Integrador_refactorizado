import pandas as pd


def limpiar_comercios(dataframe_sucio):
    # Se hace una copia para no mutar el DataFrame original que viene del API.
    dataframe_limpio = dataframe_sucio.copy()

    # Definiendo las columnas que se espera que sean de tipo texto
    columnas_texto = [
        "nombre",
        "correo",
        "direccion",
        "telefono",
        "actividad",
        "representanteLegal",
    ]

    # Se recorre cada columna de texto y se normaliza:
    #   - astype("string") para usar el tipo de string nativo de pandas
    #     (admite valores nulos sin problemas).
    #   - strip() elimina espacios al inicio y al final.
    #   - lower() lleva todo a minúsculas (útil para agrupaciones).
    for columna in columnas_texto:
        dataframe_limpio[columna] = (
            dataframe_limpio[columna]
            .astype("string")
            .str.strip()
            .str.lower()
        )

    # "sitioWeb" se trata aparte porque puede ser nulo. Si tiene valor,
    # se normaliza (strip + lower). Si está vacío, se preserva como pd.NA
    # para que el análisis de "con/sin web" sea exacto.
    dataframe_limpio["sitioWeb"] = (
        dataframe_limpio["sitioWeb"]
        .astype("string")
        .str.strip()
        .str.lower()
    )

    # Columnas numéricas: id (PK) y nit (identificador tributario).
    # Se convierten a numérico para poder filtrar y bucketizar.
    dataframe_limpio["id"] = pd.to_numeric(dataframe_limpio["id"])
    dataframe_limpio["nit"] = pd.to_numeric(dataframe_limpio["nit"])

    # Se filtran filas con valores inválidos en los identificadores.
    # En el dominio del backend, id y nit siempre deben ser positivos.
    dataframe_limpio = dataframe_limpio[
        (dataframe_limpio["id"] > 0)
        & (dataframe_limpio["nit"] > 0)
    ]

    return dataframe_limpio
