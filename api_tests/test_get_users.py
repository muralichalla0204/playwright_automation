from utils.api_client import get


def test_get_user():

    response = get("/users/2")

    assert response.status_code == 200

    data = response.json()

    assert data["data"]["first_name"] == "Janet"