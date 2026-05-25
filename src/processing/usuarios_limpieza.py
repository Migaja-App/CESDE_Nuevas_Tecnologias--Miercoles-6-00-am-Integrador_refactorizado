import pandas as pd

def limpiar_usuarios(dataframe_sucio):

    # Realizando una copia del dataframe sucio para no modificar el original
    dataframe_limpio = dataframe_sucio.copy()

    # Definiendo las columnas que se espera que sean de tipo texto
    columnas_texto = ["nombre" , "apellidos" , "tipoDocumento" , "email" , "direccion" , "rol"]
    
    # Este ciclo for se encarga de tomar cada columana de texto del dataframe y asegurarse en que sean de tipo String y en minúscula, además de eliminar los espacios en blanco.
    for columna in columnas_texto:
        dataframe_limpio[columna] = dataframe_limpio[columna].astype("string").str.strip().str.lower()
    
    # estoy creando un diccionarios con los enums esperados para cada columna, esto me ayudará a validar que los datos en esas columnas sean correctos.
    enums_esperados = {
        "tipoDocumento": ["cedula_de_ciudadania", "tarjeta_de_identidad", "cedula_de_extranjeria"],
        "rol": ["administrador" , "cliente" , "empleado"]
    }
    
    # Este ciclo for se encarga de validar que los datos en las columnas "tipoDocumento" y "rol" sean correctos, si no lo son, los reemplaza por pd.NA (valor nulo de pandas).
    for columna , valores_enums in enums_esperados.items():
        dataframe_limpio[columna] = dataframe_limpio[columna].where(dataframe_limpio[columna].isin(valores_enums), pd.NA)
    
    # convirtiendo las columnas "id" y "edad" a tipo numérico
    dataframe_limpio["id"] = pd.to_numeric(dataframe_limpio["id"])
    dataframe_limpio["edad"] = pd.to_numeric(dataframe_limpio["edad"])
    
    dataframe_limpio = dataframe_limpio[
        (dataframe_limpio["id"] > 0) &
        (dataframe_limpio["edad"] > 0)
    ]
    
    return dataframe_limpio