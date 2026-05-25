# 📊 Analytics Refactor - Pipeline de Ciencia de Datos

Este proyecto es el motor de analítica para el **Proyecto Integrador**. Se encarga de transformar datos crudos provenientes de una API backend en información visual valiosa mediante un pipeline procesado en cuatro capas.

---

## 🚀 Descripción General

El pipeline está diseñado para automatizar la extracción, limpieza, transformación y visualización de datos relacionados con **Usuarios** y **Comercios**. El resultado final son gráficos estadísticos optimizados para ser consumidos por una interfaz frontend.

## 🏗️ Arquitectura del Proyecto

El código sigue un patrón modular dividido en responsabilidades claras:

1.  **`src/api` (Consumo)**: Interactúa con los endpoints del backend para obtener datos en formato JSON y convertirlos en `Pandas DataFrames`.
2.  **`src/processing` (Limpieza)**: Normaliza textos, maneja valores nulos, valida tipos de datos (Enums) y filtra registros inconsistentes.
3.  **`src/transforming` (Transformación)**: Aplica lógica de negocio y agregaciones (filtros generacionales, promedios, conteos por categoría).
4.  **`src/visualization` (Visualización)**: Genera archivos `.png` de alta resolución utilizando `Matplotlib` y `Seaborn`.

---

## 📁 Estructura de Archivos

```text
analytics_refactor/
├── main.py                 # Punto de entrada y orquestación del pipeline
├── config.py               # Configuración de URLs y Endpoints
├── requirements.txt        # Dependencias del proyecto
└── src/
    ├── api/                # Capa de consumo de API
    ├── processing/         # Capa de limpieza y normalización
    ├── transforming/       # Capa de lógica de negocio y agregaciones
    └── visualization/      # Capa de generación de gráficos
```

---

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Manipulación de Datos:** [Pandas](https://pandas.pydata.org/)
*   **Visualización:** [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)
*   **Peticiones HTTP:** [Requests](https://requests.readthedocs.io/)

---

## ⚙️ Configuración e Instalación

1.  **Clonar el repositorio:**
    ```bash
    git clone <url-del-repositorio>
    cd analytics_refactor
    ```

2.  **Crear y activar un entorno virtual (Opcional pero recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar el Backend:**
    Asegúrate de que la API esté corriendo en `http://localhost:8080` (o ajusta el archivo `config.py`).

---

## 📈 Flujos de Trabajo

### Pipeline de Usuarios
*   **Métricas:** Distribución por rol, tipo de documento, promedios de edad y segmentación de jóvenes/adultos mayores.
*   **Salida:** Gráficos guardados en `frontend/src/assets/python/graficos/usuarios/`.

### Pipeline de Comercios
*   **Métricas:** Actividad económica, ubicación, presencia web y top de representantes.
*   **Salida:** Gráficos guardados en `frontend/src/assets/python/graficos/comercios/`.

---

## 🏁 Ejecución

Para ejecutar todo el pipeline de analítica, simplemente corre el archivo principal:

```bash
python main.py
```
