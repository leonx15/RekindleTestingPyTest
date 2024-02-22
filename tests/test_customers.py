from utils import utils_main
from utils import utils_customers
import json


class TestCustomers:

    def test_api_status_customers(self):
        response = utils_customers.api_status_customers()
        assert response.status_code == 200

    def test_create_user(self):
        user_data = {
            "username": "Test1",
            "firstName": "Testiko",
            "lastName": "Testowy"
        }

        count_before = utils_main.count_items_in_db("customer.customers")
        print(f"Count before: {count_before}")

    # Step 1: Create User.
        response, customer_id = utils_customers.create_customer(user_data)
    # Step 2: Check the message and status code from endpoint.
        assert json.loads(response.text)["message"] == "Customer saved successfully!"
        assert response.status_code == 201
    # Step 3: Check DB for created user.
        count_after = utils_main.count_items_in_db("customer.customers")
        print(f"Count after: {count_after}")
        assert count_after == count_before + 1
    # Step 4: Remove created customer.
        utils_main.remove_items_in_db("customer.customers", customer_id)
