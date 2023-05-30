import json

import pytest
import requests

post_data = {
    "name": "Roopas Doe",
    "trips": 200,
    "airline": 128116
}

put_data = {
    "name": "Roopa",
    "trips": 200,
    "airline": 128116
}


@pytest.fixture
def api_url_first():
    return "https://api.instantwebtools.net/v1/passenger"


@pytest.fixture
def api_url_third():
    return "https://api.instantwebtools.net/v1/passenger/646495f6f50535e8d633e220"


passenger_id = ''


def test_001_post_request(api_url_first):
    response = requests.post(f"{api_url_first}", data=post_data)
    data = response.json()
    assert response.status_code == 200, "Request Failed"
    str_data = json.dumps(data)
    parsed_data = json.loads(str_data)
    global passenger_id
    passenger_id = parsed_data["_id"]
    print(passenger_id)
    assert parsed_data["name"] == post_data["name"], "Failed Test"
    assert parsed_data["trips"] == post_data["trips"], "Failed Test"
    assert parsed_data["airline"][0]["id"] == post_data["airline"], "Failed Test"


def test_002_put_request():
    response = requests.put("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id), data=put_data)
    assert response.status_code == 200, "Failed Test"
    data = json.dumps(response.json())
    parsed_data = json.loads(data)
    assert parsed_data["message"] == "Passenger data put successfully completed.", "Failed Test"


def test_003_get_request():
    response = requests.get("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id))
    assert response.status_code == 200, "Failed Test"
    parsed_data = json.loads(json.dumps(response.json()))
    assert parsed_data["name"] == put_data["name"], "Failed Test"


def test_004_delete_request(api_url_third):
    response = requests.delete("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id))
    assert response.status_code == 200, "Failed Test"
    parsed_data = json.loads(json.dumps(response.json()))
    assert parsed_data["message"] == "Passenger data deleted successfully."


def test_005_get_request():
    response = requests.get("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id))
    assert response.status_code == 204, "Failed Test"
