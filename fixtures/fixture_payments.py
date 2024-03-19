from utils import utils_main, utils_payments
import pytest

schema_for_db_credit_entry = "payment.credit_entry"
schema_for_db_credit_history = "payment.credit_history"


@pytest.fixture()
def clean_up_after_add_credit(create_new_customer):
    _, customer_id = create_new_customer
    yield customer_id
    # utils_main.remove_items_in_db(schema_for_db_credit_entry, customer_id, db_column="customer_id")
    # utils_main.remove_items_in_db(schema_for_db_credit_history, customer_id, db_column="customer_id")
