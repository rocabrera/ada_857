import json

def test_home(client):
    response = client.get("/")

    assert 200 == response.status_code
    assert "ESTOU ESPERANDO REQUISICOES" == response.text
    assert "application/text" == response.mimetype


def test_predict(client, input_body):

    response = client.post("/predict", 
                           data=json.dumps(input_body),
                           content_type='application/json')
    assert 200 == response.status_code
    assert {"predicts": "[0,0,0]"} == response.get_json()
    assert "application/json" == response.mimetype


def test_invalid_predict(client, invalid_body):

    response = client.post("/predict", 
                           data=json.dumps(invalid_body),
                           content_type='application/json')

    assert 400 == response.status_code
    assert {"error": "Invalid body"} == response.get_json()
    assert "application/json" == response.mimetype
