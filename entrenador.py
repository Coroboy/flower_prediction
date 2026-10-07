import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from conexion import obtener_conexion
import joblib

conexion = obtener_conexion()
df_iris = pd.read_sql("SELECT * FROM iris", conexion)
#separar Variables "x" e "y"
x = df_iris.drop(columns=['id', 'Species'])
y = df_iris['Species']

print("ENTRENANDO EL MODELO FINAL")
modelo_produccion=DecisionTreeClassifier(random_state=42)
modelo_produccion.fit(x,y)
joblib.dump(modelo_produccion,'cerebro.joblib')
print("CEREBRO CREADO CON ÉXITO")