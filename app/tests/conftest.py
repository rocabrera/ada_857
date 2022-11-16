### Must run before importing app
import sys
from unittest.mock import MagicMock 

class FakerUtilities():

    @staticmethod
    def load_model():
        estimator = MagicMock()
        estimator.predict.return_value = "[0,0,0]"
        return estimator

sys.modules['src.utilities'] = FakerUtilities

### Testing 
import json
import pathlib
import pytest
from main import app

current_file_path = pathlib.Path(__file__)

def load_data(file_name):

    with open(current_file_path.parent / "data" / file_name, 'rb') as f:
        data = json.load(f)
        
    return data

@pytest.fixture()
def client():
    return app.test_client()

@pytest.fixture()
def input_body():
    return load_data("valid_input.json")


@pytest.fixture()
def invalid_body():
    return load_data("invalid_input.json")