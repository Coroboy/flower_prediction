import base64
import pandas as pd
import joblib 

print("EL CEREBRO SE ESTÁ CARGANDO...ESPERA")
cerebro_cargado=joblib.load('cerebro.joblib')
print("EL MODELO FUE CARGADO DE MANERA CORRECTA")
print("+"*100) 

while True:
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
        
        prediccion_final=cerebro_cargado.predict(flor_inventada)
        print(f"LA ESPECIE ES: {prediccion_final[0]}")

    except ValueError:
        print("ERROR EN LOS VALORES, NO SON VALIDOS")