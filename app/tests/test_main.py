import json

def test_home(client):

    response = client.get("/")
    assert b'ESTOU ESPERANDO REQUISICOES' == response.data
    assert 200 == response.status_code
    assert 'application/text' == response.content_type

def test_predict(client, correct_input):

    response = client.post("/predict", 
                           data=json.dumps(correct_input),
                           content_type="application/json")
 
    assert {'predicts': '[0 2]'} == response.get_json()
    assert 200 == response.status_code
    assert 'application/json' == response.content_type