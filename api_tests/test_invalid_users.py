from utils.api_client import get


def test_invalid_user():

    response = get("/users/9999")

    assert response.status_code == 404