from utils import utils_main, utils_payments
import pytest
import json

schema_for_db_credit_entry = "payment.credit_entry"
schema_for_db_credit_history = "payment.credit_history"


@pytest.fixture()
def add_credits_to_user(create_new_customer):
    _, customer_id = create_new_customer
    request_data = {
        "customerId": customer_id,
        "totalPrice": 100
    }
    _, json_response = utils_payments.add_credits_to_wallet(request_data)
    credit_entry_id = json_response['creditEntryId']
    yield credit_entry_id, customer_id
    utils_main.remove_items_in_db(schema_for_db_credit_entry, customer_id, db_column="customer_id")
    utils_main.remove_items_in_db(schema_for_db_credit_history, customer_id, db_column="customer_id")
