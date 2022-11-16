import json
import pytest
from main import app

from pathlib import Path

current_folder_path = Path(__file__).parent

@pytest.fixture()
def client():
    return app.test_client()

@pytest.fixture()
def correct_input():
    path = current_folder_path / "data" / "correct_input.json" 
    with open(path, "rb") as f:
        data = json.load(f)
    return data