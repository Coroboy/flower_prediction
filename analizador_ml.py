import pandas as pd
import joblib
from sklearn.model_selection import train_test_split  # pyright: ignore[reportMissingModuleSource]
from sklearn.tree import DecisionTreeClassifier  # pyright: ignore[reportMissingModuleSource]
from sklearn.metrics import accuracy_score, classification_report  # pyright: ignore[reportMissingModuleSource]
from conexion import obtener_conexion
from pathlib import Path


conexion = obtener_conexion()
query = "SELECT * FROM iris"
df_iris = pd.read_sql(query, conexion)
#separar Variables "x" e "y"
x = df_iris.drop(columns=['id', 'species'])
y = df_iris['species']

# Dividir el conjunto de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"Tamaño del conjunto de entrenamiento son : {len(x_train)}")
print(f"Tamaño del conjunto de prueba son : {len(x_test)}")

# Crear el modelo de árbol de decisión
modelo_arbol = DecisionTreeClassifier(random_state=42)

# Entrenar el modelo con los datos de entrenamiento
modelo_arbol.fit(x_train, y_train)

# Realizar predicciones con los datos de prueba
predicciones = modelo_arbol.predict(x_test)

# Calcular la precisión del modelo
precision = accuracy_score(y_test, predicciones)
print(f"Precisión del modelo: {precision * 100:.2f}%")
print("Reporte de clasificación:")
print(classification_report(y_test, predicciones))

ruta_modelo = Path(__file__).with_name("nuevocerebro.joblib")
joblib.dump(modelo_arbol, ruta_modelo)
print(f"Modelo guardado en: {ruta_modelo}")

while True:
    print("\nIngrese las medidas de la flor o escriba 'salir' para terminar:")
    try:
        dato1 = input("Ingrese el valor de la primera característica (longitud del sépalo): ")
        if dato1.strip().lower() == "salir":
            break
        sepallength = float(dato1)

        dato2 = input("Ingrese el valor de la segunda característica (anchura del sépalo): ")
        if dato2.strip().lower() == "salir":
            break
        sepalwidth = float(dato2)

        dato3 = input("Ingrese el valor de la tercera característica (longitud del pétalo): ")
        if dato3.strip().lower() == "salir":
            break
        petallength = float(dato3)

        dato4 = input("Ingrese el valor de la cuarta característica (anchura del pétalo): ")
        if dato4.strip().lower() == "salir":
            break
        petalwidth = float(dato4)

        flor_inventada = pd.DataFrame([[
            sepallength,
            sepalwidth,
            petallength,
            petalwidth
        ]], columns=x.columns)

        prediccion_final = modelo_arbol.predict(flor_inventada)[0]
        print(f"La especie predicha para la flor ingresada es: {prediccion_final}")

        continuar = input("¿Desea clasificar otra flor? (s/n): ")
        if continuar.strip().lower() != "s":
            break
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para las características de la flor.")