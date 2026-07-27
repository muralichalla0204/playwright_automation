from utils.api_client import patch
from test_data.payloads import UPDATE_USER


def test_update_user():

    response = patch("/users/2", UPDATE_USER)

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == UPDATE_USER["name"]
    assert data["job"] == UPDATE_USER["job"]

    assert "updatedAt" in data