import pandas as pd
from flask import Flask, request
from src.utilities import load_model

app = Flask(__name__)
estimator = load_model()

@app.route('/',  methods=['GET'])
def home():
    return "ESTOU ESPERANDO REQUISICOES"

@app.route('/predict', methods=['POST'])
def predict():

    body = request.get_json()
    
    X = pd.DataFrame(body)
    y = estimator.predict(X)

    return f'Feature, Predita {y}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
