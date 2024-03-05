from utils import utils_customers
from fixtures.fixture_customers import user_data, create_new_customer



class TestCustomers:

    def test_api_status_customers(self):
        response = utils_customers.get_list_of_customers()[0]
        assert response.status_code == 200

    def test_create_user(self, create_new_customer):

        response, customer_id = create_new_customer
        assert response.status_code == 201
        response, _ = utils_customers.get_customer_data(customer_id)
        assert response.status_code == 200

    def test_update_customer(self, create_new_customer, user_data):
        # Step 1: Create user.
        _, customer_id = create_new_customer
        _, update_user_data = user_data
        _, created_user_data = utils_customers.get_customer_data(customer_id)
        utils_customers.update_customer(customer_id, update_user_data)
        # Step 2: Check updated values.
        _, updated_user_data = utils_customers.get_customer_data(customer_id)
        assert created_user_data["id"] == updated_user_data["id"]
        assert updated_user_data["username"] == update_user_data["username"]
        assert updated_user_data["firstName"] == update_user_data["firstName"]
        assert updated_user_data["lastName"] == update_user_data["lastName"]


    def test_delete_customer_by_api(self, user_data):
        # Step 1: Create user.
        new_customer_data, _ = user_data
        _, customer_id = utils_customers.create_customer(new_customer_data)
        response, _ = utils_customers.get_customer_data(customer_id)
        assert response.status_code == 200
        # Step 2: Delete created user.
        response = utils_customers.delete_customer(customer_id)
        assert response.status_code == 200
        # Step 3: Check if user cannot be reach by API.
        response, _ = utils_customers.get_customer_data(customer_id, allowed_statuses=[400])
        assert response.status_code == 400, "Customer data still available after deletion."
