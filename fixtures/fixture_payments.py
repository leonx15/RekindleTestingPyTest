import pytest
from utils import utils_main, utils_payments

@pytest.fixture()
def add_credits_to_user(create_new_customer):
    customer_id = "12314144234"
    return customer_id