# Must run before testing
import sys
from unittest.mock import Mock


class FakeUtilities:
    @staticmethod
    def load_model():
        estimator = Mock()
        estimator.predict.return_value = [0, 0]
        return estimator


sys.modules["src.utilities"] = FakeUtilities

import json
import pytest
from main import app

from pathlib import Path

data_folder_path = Path(__file__).parent / "data"


def load_data(path):
    with open(path, "rb") as f:
        data = json.load(f)
    return data


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def correct_input():
    path = data_folder_path / "correct_input.json"

    return load_data(path)


@pytest.fixture()
def invalid_input():
    path = data_folder_path / "invalid_input.json"

    return load_data(path)
