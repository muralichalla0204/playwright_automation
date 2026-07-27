from utils.api_client import delete


def test_delete_user():

    response = delete("/users/2")

    assert response.status_code == 204