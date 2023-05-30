import pytest
import json
import requests


@pytest.mark.usefixtures("fixture")
@pytest.mark.parametrize("page,size", [(0, 10), (1, 5), (2, 3)])
def test_001_parametrize_test(page, size):
    response = requests.get("https://api.instantwebtools.net/v1/passenger?page="+str(page)+"&size="+str(size))
    assert response.status_code == 200, "Failed Test"
    parsed_data = json.loads(json.dumps(response.json()))
    assert len(parsed_data["data"]) == size, "Failed Test"
    print(parsed_data)

