# Clasificador de flores Iris

Proyecto de análisis y clasificación de flores Iris con Python, MySQL y un
árbol de decisión.

## Preparación

1. Crea la base de datos `iris_db` y la tabla `iris` con las columnas
   `id`, `sepallengthcm`, `sepalwidthcm`, `petallengthcm`, `petalwidthcm` y
   `species`.
2. Activa el entorno virtual e instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

3. Copia `.env.example` como `.env` y configura tus variables de conexión.
   También puedes exportarlas directamente en la terminal.

## Uso

Desde esta carpeta, ejecuta `analizador_ml.py` para consultar los datos,
entrenar el árbol, mostrar su evaluación y guardar `nuevocerebro.joblib`.
Después ejecuta `app_prediction.py` para clasificar nuevas flores.

`analizador.py` genera estadísticas y gráficas exploratorias a partir de la
tabla `iris`.
