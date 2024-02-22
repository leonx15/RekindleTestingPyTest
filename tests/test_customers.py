from utils import utils_main
from utils import utils_customers

import requests
import json


class TestCustomers:

    def test_api_status_customers(self):
        host = utils_main.load_config()["host_env"]
        headers = {
            "Authorization": f"Bearer {utils_main.get_jwt_token()}"
        }
        response = requests.get(f"http://{host}:8184/api/v1/customers", headers=headers)
        assert response.status_code == 200

    def test_create_user(self):
        host = utils_main.load_config()["host_env"]
        count_before = utils_main.count_items_in_db("customer.customers")
        print(f"Count before: {count_before}")

        # Set up to create new user by API request.
        response = utils_customers.create_customer(host)
        customer_id = json.loads(response.text)["customerId"]
        print(f"User created: {customer_id}")
        # Check the message and status code from endpoint.
        assert json.loads(response.text)["message"] == "Customer saved successfully!"
        assert response.status_code == 201
        count_after = utils_main.count_items_in_db("customer.customers")
        print(f"Count after: {count_after}")

        # Check if user is created in the DB.
        assert count_after == count_before + 1

        # Remove created customer from previous steps.
        utils_main.remove_items_in_db("customer.customers", customer_id)
