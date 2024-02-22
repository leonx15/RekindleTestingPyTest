from utils import utils_main
import requests
import json

host = utils_main.load_config()["host_env"]
headers = {
        "Authorization": f"Bearer {utils_main.get_jwt_token()}"
    }


def api_status_customers():
    response = requests.get(f"http://{host}:8184/api/v1/customers", headers=headers)
    return response


def create_customer(json_data):
    try:
        response = requests.post(f"http://{host}:8184/api/v1/customers", json=json_data, headers=headers)
        response.raise_for_status()
        customer_id = json.loads(response.text)["customerId"]
        print(f"User created: {customer_id}")
        return response, customer_id
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


def update_customer(customer_id, json_data):
    try:
        response = requests.put(f"http://{host}:8184/api/v1/customers/{customer_id}", json=json_data, headers=headers)
        response.raise_for_status()
        print(f"User updated: {customer_id}")
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")



def delete_customer(customer_id):
    try:
        response = requests.delete(f"http://{host}:8184/api/v1/customers/{customer_id}")
        print(f"User {customer_id} successfully deleted")
        return response
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")