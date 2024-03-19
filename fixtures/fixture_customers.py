from utils import utils_customers
import pytest
from faker import Faker

schema_for_db_customers = "customer.customers"


@pytest.fixture()
def customer_data():
    fake = Faker()
    new_customer_data = {
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name()
    }
    updated_customer_data = {
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name()
    }
    return new_customer_data, updated_customer_data


@pytest.fixture()
def create_new_customer(customer_data):
    new_customer_data, _ = customer_data
    response, customer_id = utils_customers.create_customer(new_customer_data)
    yield response, customer_id
    # utils_main.remove_items_in_db(schema_for_db_customers, customer_id)
