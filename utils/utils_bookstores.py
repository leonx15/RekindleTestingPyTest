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
        bookstore_id = json.loads(response.text)
        return response, bookstore_id
    except requests.exceptions.HTTPError as http_err:
        raise AssertionError(f"HTTP error during creating bookstore: {http_err}")
    except Exception as err:
        raise AssertionError(f"An error occurred: {err}")


def get_specific_bookstore(bookstore_id):
    try:
        response = requests.get(f"http://{host}:8183/api/v1/bookstores/{bookstore_id}", headers=headers)
        bookstore_data = None
        if response.status_code == 200:
            bookstore_data = json.loads(response.text)
        elif response.status_code == 404:
            print(f"Bookstore id {bookstore_id} response is 404")
            return response, bookstore_data
        response.raise_for_status()
        return response, bookstore_data
    except requests.exceptions.HTTPError as http_err:
        raise AssertionError(f"HTTP error during looking for bookstore: {http_err}")
    except Exception as err:
        raise AssertionError(f"An error occurred: {err}")


def update_bookstore(bookstore_id, json_data):
    try:
        response = requests.put(f"http://{host}:8183/api/v1/bookstores/{bookstore_id}", json=json_data, headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        raise AssertionError(f"HTTP error during looking for bookstore: {http_err}")
    except Exception as err:
        raise AssertionError(f"An error occurred: {err}")

def delete_bookstore(bookstore_id):
    try:
        response = requests.delete(f"http://{host}:8183/api/v1/bookstores/{bookstore_id}", headers=headers)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as http_err:
        raise AssertionError(f"HTTP error during looking for bookstore: {http_err}")
    except Exception as err:
        raise AssertionError(f"An error occurred: {err}")