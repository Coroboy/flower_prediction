from analizador_ml import mArbol
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from conexion import obtener_conexion


conexion = obtener_conexion()
query = "SELECT * FROM iris"
df_iris = pd.read_sql(query, conexion)
#separar Variables "x" e "y"
x = df_iris.drop(columns=['Id', 'Species'])
y = df_iris['Species']

# Dividir el conjunto de datos en entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"Tamaño del conjunto de entrenamiento son : {len(x_train)}")
print(f"Tamaño del conjunto de prueba son : {len(x_test)}")

# Crear el modelo de árbol de decisión
model_arbll = DecisionTreeClassifier(random_state=42)

# Entrenar el modelo con los datos de entrenamiento
model_arbll.fit(x_train, y_train)



while True:
    # Solicitar al usuario que ingrese los valores de las características
    print("ml para clasificar especies de flor  iris:")
    print("escriba 'salir' para terminar el programa.")
    try:
        dato1 = input("Ingrese el largo del sépalo (cm): ")
        if dato1.lower() == 'salir':
            break
        sepal_length = float(dato1)

        dato2 = input("Ingrese el ancho del sépalo (cm): ")
        if dato2.lower() == 'salir':
            break
        sepal_width = float(dato2)

        dato3 = input("Ingrese el largo del pétalo (cm): ")
        if dato3.lower() == 'salir':
            break
        petal_length = float(dato3)

        dato4 = input("Ingrese el ancho del pétalo (cm): ")
        if dato4.lower() == 'salir':
            break
        petal_width = float(dato4)

        flor_inventada=pd.DataFrame([{
            'SepalLengthCm':sepal_length,
            'SepalWidthCm':sepal_width,
            'PetalLengthCm':petal_length,
            'PetalWidthCm':petal_width
        }])
        
        prediccion_final=mArbol.predict(flor_inventada)
        print(f"LA ESPECIE ES: {prediccion_final[0]}")

    except ValueError:
        print("ERROR EN LOS VALORES, NO SON VALIDOS")