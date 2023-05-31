import json

import pytest
import requests

from log_file import log_class


@pytest.fixture
def api_url_first():
    return "https://api.instantwebtools.net/v1/passenger"


@pytest.mark.usefixtures("setup")
class TestApi(log_class):
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

    passenger_id = ''

    def test_001_post_request(self, api_url_first):
        log = self.test_log()
        log.info("First Api test started for Post Request")
        response = requests.post(f"{api_url_first}", data=self.post_data)
        data = response.json()
        assert response.status_code == 200, "Request Failed"
        log.info("Status Code asserted successfully for test_001")
        str_data = json.dumps(data)
        parsed_data = json.loads(str_data)
        global passenger_id
        passenger_id = parsed_data["_id"]
        print(self.passenger_id)
        assert parsed_data["name"] == self.post_data["name"], "Failed Test"
        assert parsed_data["trips"] == self.post_data["trips"], "Failed Test"
        assert parsed_data["airline"][0]["id"] == self.post_data["airline"], "Failed Test"
        log.info("Response Data asserted successfully for test_001")

    def test_002_put_request(self):
        log = self.test_log()
        log.info("Second Test with put request started")
        response = requests.put("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id),
                                data=self.put_data)
        assert response.status_code == 200, "Failed Test"
        log.info("Status code asserted for test_002")
        data = json.dumps(response.json())
        parsed_data = json.loads(data)
        assert parsed_data["message"] == "Passenger data put successfully completed.", "Failed Test"
        log.info("Response Data asserted successfully for test_002")

    def test_003_get_request(self):
        log = self.test_log()
        response = requests.get("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id))
        assert response.status_code == 200, "Failed Test"
        parsed_data = json.loads(json.dumps(response.json()))
        assert parsed_data["name"] == self.put_data["name"], "Failed Test"
        log.info("Response Data asserted successfully for test_003")

    def test_004_delete_request(self):
        log = self.test_log()
        response = requests.delete("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id))
        assert response.status_code == 200, "Failed Test"
        parsed_data = json.loads(json.dumps(response.json()))
        assert parsed_data["message"] == "Passenger data deleted successfully."
        log.info("Response Data asserted successfully for test_004")

    def test_005_get_request(self):
        log = self.test_log()
        response = requests.get("https://api.instantwebtools.net/v1/passenger/" + str(passenger_id))
        assert response.status_code == 204, "Failed Test"
