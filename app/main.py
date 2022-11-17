import json
import pandas as pd
from flask import Flask, request, Response
from src.utilities import load_model
from src.exceptions import exception_handler, PredictionError

app = Flask(__name__)
estimator = load_model()

@app.errorhandler(Exception)
def handle_bad_request(e):
    return exception_handler(e)

@app.route('/',  methods=['GET'])
def home():
    return Response(
        response="ESTOU ESPERANDO REQUISICOES",
        status=200,
        content_type='application/text'
    )

@app.route('/predict', methods=['POST'])
def predict():
    try:

        body = request.get_json()
        X = pd.DataFrame(body)
        y = estimator.predict(X)

    except Exception:
        raise PredictionError("Check the body requisition")

    else:
        return Response(
            response=json.dumps({"predicts": str(y)}),
            status=200,
            content_type='application/json'
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
