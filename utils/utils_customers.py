from utils import utils_main
import requests
import json

def api_status_customers():
    host = utils_main.load_config()["host_env"]
    headers = {
        "Authorization": f"Bearer {utils_main.get_jwt_token()}"
    }
    response = requests.get(f"http://{host}:8184/api/v1/customers", headers=headers)
    return response


def create_customer(json_data):
    host = utils_main.load_config()["host_env"]
    headers = {
        "Authorization": f"Bearer {utils_main.get_jwt_token()}"
    }

    response = requests.post(f"http://{host}:8184/api/v1/customers", json=json_data, headers=headers)
    customer_id = json.loads(response.text)["customerId"]
    print(f"User created: {customer_id}")
    return response, customer_id
