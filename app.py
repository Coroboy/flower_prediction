from flask import Flask, render_template, request
import pandas as pd
import joblib
from pathlib import Path

app=Flask(__name__)
#cargar el modelo cuando se inicia el servidor
modelo=joblib.load(Path(__file__).with_name('nuevocerebro.joblib'))

FEATURES = {
    'sepal_length': 'sepallengthcm',
    'sepal_width': 'sepalwidthcm',
    'petal_length': 'petallengthcm',
    'petal_width': 'petalwidthcm',
}

def render_inicio(**context):
    return render_template('index.html', **context)

@app.route('/',methods=['GET'])
def inicio():
    return render_inicio()
@app.route('/predecir',methods=['POST'])
def predecir():
    valores = {campo: request.form.get(campo, '').strip() for campo in FEATURES}
    try:
        datos = {columna: [float(valores[campo])] for campo, columna in FEATURES.items()}
        columnas_modelo = list(getattr(modelo, 'feature_names_in_', FEATURES.values()))
        df = pd.DataFrame(datos).reindex(columns=columnas_modelo)

        prediccion = modelo.predict(df)[0]
        confianza = None
        if hasattr(modelo, 'predict_proba'):
            confianza = round(float(modelo.predict_proba(df).max() * 100), 1)
        return render_inicio(prediccion=prediccion, confianza=confianza, valores=valores)
    except (TypeError, ValueError):
        return render_inicio(
            error="Revisa los datos: introduce un número válido en cada medida.",
            valores=valores,
        )

if __name__ == '__main__':
    app.run(debug=True, port=5001)