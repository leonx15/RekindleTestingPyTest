import pytest
from utils import utils_main, utils_customers


@pytest.fixture()
def setup_schema_for_db():
    schema_for_db = "customer.customers"
    return schema_for_db


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


@pytest.fixture()
def create_new_customer(user_data, setup_schema_for_db):
    new_user_data, _ = user_data
    response, customer_id = utils_customers.create_customer(new_user_data)
    yield response, customer_id
    utils_main.remove_items_in_db(setup_schema_for_db, customer_id)
