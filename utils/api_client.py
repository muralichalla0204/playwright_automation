import requests

from utils.config_reader import get_api_base_url, get_api_key


def _headers():
    return {"x-api-key": get_api_key()}


def get(endpoint):
    return requests.get(f"{get_api_base_url()}{endpoint}", headers=_headers())


def post(endpoint, payload):
    return requests.post(
        f"{get_api_base_url()}{endpoint}", json=payload, headers=_headers()
    )


def patch(endpoint, payload):
    return requests.patch(
        f"{get_api_base_url()}{endpoint}", json=payload, headers=_headers()
    )


def delete(endpoint):
    return requests.delete(f"{get_api_base_url()}{endpoint}", headers=_headers())
