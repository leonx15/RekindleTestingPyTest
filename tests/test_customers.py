from utils import utils_main
from utils import utils_customers
import json
import pytest

schema_for_db = "customer.customers"
@pytest.fixture()
def user_data():
    return {
            "username": "Test1",
            "firstName": "Testiko",
            "lastName": "Testowy"
        }

class TestCustomers:

    def test_api_status_customers(self):
        response = utils_customers.api_status_customers()
        assert response.status_code == 200

    def test_create_user(self, user_data):

        count_before = utils_main.count_items_in_db(schema_for_db)
        print(f"Count before: {count_before}")

    # Step 1: Create User.
        response, customer_id = utils_customers.create_customer(user_data)
    # Step 2: Check the message and status code from endpoint.
        assert json.loads(response.text)["message"] == "Customer saved successfully!"
        assert response.status_code == 201
    # Step 3: Check DB for created user.
        count_after = utils_main.count_items_in_db(schema_for_db)
        print(f"Count after: {count_after}")
        assert count_after == count_before + 1
    # Step 4: Remove created customer.
        utils_main.remove_items_in_db(schema_for_db, customer_id)

    def test_update_customer(self, user_data):
        _, customer_id = utils_customers.create_customer(user_data)
        new_user_data = {
            "username": "UpTest1",
            "firstName": "UpTestiko",
            "lastName": "UpTestowy"
        }
        _, created_user_data = utils_customers.get_customer_data(customer_id)
        utils_customers.update_customer(customer_id, new_user_data)
        _, updated_user_data = utils_customers.get_customer_data(customer_id)
        assert created_user_data != updated_user_data

        utils_main.remove_items_in_db(schema_for_db, customer_id)

    def test_delete_customer_by_api(self, user_data):
        _, customer_id = utils_customers.create_customer(user_data)
        response, _ = utils_customers.get_customer_data(customer_id)
        assert response.status_code == 200
        response = utils_customers.delete_customer(customer_id)
        assert response.status_code == 200
        try:
            response, _ = utils_customers.get_customer_data(customer_id)
            assert response.status_code == 400
        except AssertionError:
            pytest.fail("Customer data still available.")
