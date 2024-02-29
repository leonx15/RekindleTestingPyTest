from utils import utils_main
from utils import utils_customers
import json
import pytest

schema_for_db = "customer.customers"


@pytest.fixture()
def user_data():
    new_user_data = {
        "username": "Test1",
        "firstName": "Testiko",
        "lastName": "Testowy"
    }
    updated_user_data = {
        "username": "UpdateTesto",
        "firstName": "UpdateFirst",
        "lastName": "UpdateLast"
    }
    return new_user_data, updated_user_data



class TestCustomers:

    def test_api_status_customers(self):
        response = utils_customers.get_list_of_customers()[0]
        assert response.status_code == 200

    def test_create_user(self, user_data):

        # Step 1: Count users before create new one.
        count_before = utils_main.count_items_in_db(schema_for_db)
        print(f"Count before: {count_before}")
        # Step 2: Create User.
        response, customer_id = utils_customers.create_customer(user_data[0])
        # Step 3: Check the message and status code from endpoint.
        assert json.loads(response.text)["message"] == "Customer saved successfully!"
        assert response.status_code == 201
        # Step 4: Check DB for created user.
        count_after = utils_main.count_items_in_db(schema_for_db)
        print(f"Count after: {count_after}")
        assert count_after == count_before + 1
        # Step 5: Clean up after test.
        utils_main.remove_items_in_db(schema_for_db, customer_id)

    def test_update_customer(self, user_data):
        # Step 1: Create user.
        _, customer_id = utils_customers.create_customer(user_data[0])
        _, created_user_data = utils_customers.get_customer_data(customer_id)
        utils_customers.update_customer(customer_id, user_data[1])
        # Step 3: Check updated values.
        _, updated_user_data = utils_customers.get_customer_data(customer_id)
        assert created_user_data["id"] == updated_user_data["id"]
        assert updated_user_data["username"] == user_data[1]["username"]
        assert updated_user_data["firstName"] == user_data[1]["firstName"]
        assert updated_user_data["lastName"] == user_data[1]["lastName"]
        # Step 4: Clean up after test.
        utils_main.remove_items_in_db(schema_for_db, customer_id)

    def test_delete_customer_by_api(self, user_data):
        # Step 1: Create user.
        _, customer_id = utils_customers.create_customer(user_data[0])
        response, _ = utils_customers.get_customer_data(customer_id)
        assert response.status_code == 200
        # Step 2: Delete created user.
        response = utils_customers.delete_customer(customer_id)
        assert response.status_code == 200
        # Step 3: Check if user cannot be reach by API.
        response, _ = utils_customers.get_customer_data(customer_id, allowed_statuses=[400])
        assert response.status_code == 400, "Customer data still available after deletion."
