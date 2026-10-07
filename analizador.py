import matplotlib.pyplot as plt
import pandas as pd

from conexion import obtener_conexion

def cargar_datos():
    conexion = obtener_conexion()
    return pd.read_sql("SELECT * FROM iris", conexion)


df = cargar_datos()
print("Estas son las primeras 5 filas del DataFrame:")
print(df.head())

estadisticas = df.groupby("species")[
    ["sepallengthcm", "sepalwidthcm", "petallengthcm", "petalwidthcm"]
].agg(["min", "max", "mean"])
print("Estadísticas de las medidas por especie:")
print(estadisticas)

df_setosa = df[df["species"] == "Iris-setosa"]
df_versicolor = df[df["species"] == "Iris-versicolor"]
df_virginica = df[df["species"] == "Iris-virginica"]

print("Estas son las medidas de Iris-setosa:")
print(df_setosa.head())
print("Estas son las medidas de Iris-versicolor:")
print(df_versicolor.head())
print("Estas son las medidas de Iris-virginica:")
print(df_virginica.head())




plt.figure(figsize=(10, 6))
plt.scatter(df_setosa['sepallengthcm'], df_setosa['sepalwidthcm'], color='blue', label='Iris-setosa')
plt.title('Relación entre largo y ancho del sépalo de Iris-setosa')
plt.xlabel('Largo del sépalo (cm)')
plt.ylabel('Ancho del sépalo (cm)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df_versicolor['sepallengthcm'], df_versicolor['sepalwidthcm'], color='green', label='Iris-versicolor')
plt.title('Relación entre largo y ancho del sépalo de Iris-versicolor')
plt.xlabel('Largo del sépalo (cm)')
plt.ylabel('Ancho del sépalo (cm)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df_virginica['sepallengthcm'], df_virginica['sepalwidthcm'], color='red', label='Iris-virginica')
plt.title('Relación entre largo y ancho del sépalo de Iris-virginica')
plt.xlabel('Largo del sépalo (cm)')
plt.ylabel('Ancho del sépalo (cm)')
plt.grid(True)
plt.legend()
plt.show()