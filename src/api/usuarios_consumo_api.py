import requests
import pandas as pd
from config import BASE_URL , ENDPOINTS

# Este módulo está a cargo de consumir el API del backend para obtener los datos.

def obtener_usuarios():
    url = BASE_URL + ENDPOINTS["usuarios"]
    response = requests.get(url)
    response.raise_for_status()
    return pd.DataFrame(response.json())