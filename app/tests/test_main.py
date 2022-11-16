import json


def test_home(client):

    response = client.get("/")
    assert b'ESTOU ESPERANDO REQUISICOES' == response.data
    assert 200 == response.status_code
    assert 'application/text' == response.content_type

def test_predict(client):

    body = [
        {
        "sepal length (cm)": 7.2,
        "sepal width (cm)": 0.4,
        "petal length (cm)": 0.2,
        "petal width (cm)": 0.01
        }, 
        {
        "sepal length (cm)": 7.2,
        "sepal width (cm)": 20.4,
        "petal length (cm)": 20.2,
        "petal width (cm)": 0.01
        }
    ]

    response = client.post("/predict", 
                           data=json.dumps(body),
                           content_type="application/json")
 
    assert {'predicts': '[0 2]'} == response.get_json()
    assert 200 == response.status_code
    assert 'application/json' == response.content_type