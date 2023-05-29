import json

import pytest
import requests


@pytest.fixture
def api_url():
    return "https://api.instantwebtools.net/v1/airlines/1"


@pytest.fixture
def api_url_second():
    return "https://api.instantwebtools.net/v1/passenger?page=0&size=10"


@pytest.fixture
def api_url_third():
    return "https://api.instantwebtools.net/v1/passenger?page=0&size=2"


def test_001_get_response(api_url):
    response = requests.get(f"{api_url}")
    data = response.json()
    str_data = json.dumps(data)
    parsed_data = json.loads(str_data)
    assert response.status_code == 200, "Failed Test"
    print(parsed_data)


def test_002_get_response(api_url_second):
    response = requests.get(f"{api_url_second}")
    data = response.json()
    str_data = json.dumps(data)
    parsed_data = json.loads(str_data)
    assert response.status_code == 200, "Failed Test"
    print(parsed_data)


def test_003_get_response(api_url_third):
    response = requests.get(f"{api_url_third}")
    data = response.json()
    str_data = json.dumps(data)
    parsed_data = json.loads(str_data)
    assert response.status_code == 200, "Failed Test"
    print(parsed_data)
    assert len(parsed_data["data"]) == 2, "Failed Test"
