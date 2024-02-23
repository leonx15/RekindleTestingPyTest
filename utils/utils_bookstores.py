from utils import utils_main
import requests
import json

host = utils_main.load_config()["host_env"]
headers = {
        "Authorization": f"Bearer {utils_main.get_jwt_token()}"
    }


def get_list_of_bookstores():
    try:
        response = requests.get(f"http://{host}:8183/api/v1/bookstores", headers=headers)
        response.raise_for_status()
        json_list_bookstores = json.loads(response.text)
        return response, json_list_bookstores
    except requests.exceptions.HTTPError as http_err:
        raise AssertionError(f"HTTP error occurred: {http_err}")
    except Exception as err:
        raise AssertionError(f"An error occurred: {err}")


def create_bookstore(json_data):
    try:
        response = requests.post(f"http://{host}:8183/api/v1/bookstores", json=json_data, headers=headers)
        response.raise_for_status()
        bookstore_id = response.text
        return response, bookstore_id
    except requests.exceptions.HTTPError as http_err:
        raise AssertionError(f"HTTP error during creating bookstore: {http_err}")
    except Exception as err:
        raise AssertionError(f"An error occurred: {err}")


def get_specific_bookstore(bookstore_id):
    try:
        response = requests.get(f"http://{host}:8183/api/v1/bookstores", headers=headers)
        response.raise_for_status()
        bookstore_data = json.loads(response.text)
        return response, bookstore_data
    except requests.exceptions.HTTPError as http_err:
        raise AssertionError(f"HTTP error during looking for bookstore: {http_err}")
    except Exception as err:
        raise AssertionError(f"An error occurred: {err}")