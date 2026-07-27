import requests

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "free_user_3H4urqHhDSa5KKFXfyB3QVOi2ui"
}


def get(endpoint):
    return requests.get(BASE_URL + endpoint, headers=HEADERS)


def post(endpoint, payload):
    return requests.post(BASE_URL + endpoint, json=payload, headers=HEADERS)


def patch(endpoint, payload):
    return requests.patch(BASE_URL + endpoint, json=payload, headers=HEADERS)


def delete(endpoint):
    return requests.delete(BASE_URL + endpoint, headers=HEADERS)