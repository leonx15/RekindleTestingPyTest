from utils import utils_main, utils_customers
import pytest

schema_for_db_customers = "customer.customers"


@pytest.fixture()
def customer_data():
    new_customer_data = {
        "username": "Test1",
        "firstName": "Testiko",
        "lastName": "Testowy"
    }
    updated_customer_data = {
        "username": "UpdateTesto",
        "firstName": "UpdateFirst",
        "lastName": "UpdateLast"
    }
    return new_customer_data, updated_customer_data


@pytest.fixture()
def create_new_customer(customer_data):
    new_customer_data, _ = customer_data
    response, customer_id = utils_customers.create_customer(new_customer_data)
    yield response, customer_id
    utils_main.remove_items_in_db(schema_for_db_customers, customer_id)
