from utils.api_client import post
from test_data.payloads import CREATE_USER


def test_create_user():

    response = post("/users", CREATE_USER)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == CREATE_USER["name"]
    assert data["job"] == CREATE_USER["job"]

    assert "id" in data
    assert "createdAt" in data