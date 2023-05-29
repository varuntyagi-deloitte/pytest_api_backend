import pytest

import requests


@pytest.fixture
def api_url():
    return "https://api.instantwebtools.net/v1/airlines"


def test_get_user(api_url):
    response = requests.get(f"{api_url}")
    assert response.status_code == 200
