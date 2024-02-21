from utils import get_jwt_token as jwt_token
from utils import count_items_in_db
from utils import remove_items_in_db
from utils import load_config
import requests
import json


class TestCustomers:

    def test_api_status_customers(self):
        host = load_config()["host_env"]
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        response = requests.get(f"http://{host}:8184/api/v1/customers", headers=headers)
        assert response.status_code == 200

    def test_create_user(self):
        host = load_config()["host_env"]
        count_before = count_items_in_db("customer.customers")
        print(f"Count before: {count_before}")
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        json_data = {
            "username": "Test1",
            "firstName": "Testiko",
            "lastName": "Testowy"
        }

        response = requests.post(f"http://{host}:8184/api/v1/customers", json=json_data, headers=headers)
        user_id = json.loads(response.text)["customerId"]
        print(f"User created: {user_id}")
        assert json.loads(response.text)["message"] == "Customer saved successfully!"
        assert response.status_code == 201
        count_after = count_items_in_db("customer.customers")
        print(f"Count after: {count_after}")

        assert count_after == count_before + 1

        remove_items_in_db("customer.customers", user_id)
