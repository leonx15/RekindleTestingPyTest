from utils import utils_main
import requests
import json

host = utils_main.load_config()["host_env"]
headers = {
        "Authorization": f"Bearer {utils_main.get_jwt_token()}"
    }


def get_list_of_bookstores():
    response = utils_main.make_api_request("GET", f"http://{host}:8183/api/v1/bookstores")
    json_list_bookstores = json.loads(response.text)
    return response, json_list_bookstores


def create_bookstore(json_data):
    response = utils_main.make_api_request("POST", f"http://{host}:8183/api/v1/bookstores", json_data)
    bookstore_id = json.loads(response.text)
    return response, bookstore_id


def get_specific_bookstore(bookstore_id, allowed_statuses=None):
    response = utils_main.make_api_request("GET", f"http://{host}:8183/api/v1/bookstores/{bookstore_id}", allowed_statuses=allowed_statuses)
    bookstore_data = json.loads(response.text)
    return response, bookstore_data


def update_bookstore(bookstore_id, json_data):
    response = utils_main.make_api_request("PUT", f"http://{host}:8183/api/v1/bookstores/{bookstore_id}", json_data)
    return response


def delete_bookstore(bookstore_id):
    response = utils_main.make_api_request("DELETE", f"http://{host}:8183/api/v1/bookstores/{bookstore_id}")
    response.raise_for_status()
    return response