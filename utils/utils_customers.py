from utils import utils_main
import requests
import json

host = utils_main.load_config()["host_env"]


def create_customer(json_data):
    response = utils_main.make_api_request("POST", f"http://{host}:8184/api/v1/customers", json_data)
    customer_id = json.loads(response.text)["customerId"]
    print(f"User created: {customer_id}")
    return response, customer_id


def get_list_of_customers():
    response = utils_main.make_api_request("GET", f"http://{host}:8184/api/v1/customers")
    json_list_customers = json.loads(response.text)
    return response, json_list_customers


def update_customer(customer_id, json_data):
    response = utils_main.make_api_request("PUT", f"http://{host}:8184/api/v1/customers/{customer_id}", json_data)
    print(f"User updated: {customer_id}")
    return response


def get_customer_data(customer_id, allowed_statuses=None):
    response = utils_main.make_api_request("GET", f"http://{host}:8184/api/v1/customers/{customer_id}", allowed_statuses=allowed_statuses)
    user_data = response.json()
    return response, user_data


def delete_customer(customer_id):
    response = utils_main.make_api_request("DELETE", f"http://{host}:8184/api/v1/customers/{customer_id}")
    print(f"User {customer_id} successfully deleted")
    return response
