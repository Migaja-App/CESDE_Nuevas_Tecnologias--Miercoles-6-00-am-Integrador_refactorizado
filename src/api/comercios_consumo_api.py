import requests
import pandas as pd
from config import BASE_URL, ENDPOINTS

# Este módulo se encarga de consumir el API del backend Spring (MigajaApp)
# para obtener el listado de comercios registrados y entregarlo como un
# DataFrame de pandas listo para procesar en las siguientes capas.


def obtener_comercios():
    # Se arma la URL completa concatenando la URL base del backend
    # con el endpoint específico de comercios definido en config.py.
    url = BASE_URL + ENDPOINTS["comercios"]

    # Se hace la petición HTTP GET al backend.
    response = requests.get(url)

    # Si la respuesta no es exitosa (códigos 4xx/5xx) se lanza una excepción
    # para detener el flujo en lugar de seguir con datos inválidos.
    response.raise_for_status()

    # El backend devuelve una lista JSON de objetos Comercio. Se convierte
    # directamente a DataFrame para trabajar con pandas en las capas
    # de limpieza, transformación y visualización.
    return pd.DataFrame(response.json())
