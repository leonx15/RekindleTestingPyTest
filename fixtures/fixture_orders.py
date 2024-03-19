from utils import utils_main, utils_orders, utils_payments
import pytest
from faker import Faker

schema_for_db_payment_payments = "payment.payments"
schema_for_db_order_orders = "\"order\".orders"
schema_for_db_order_order_items = "\"order\".order_items"
schema_for_db_order_order_address = "\"order\".order_address"

fake = Faker('pl_PL')
address_data = {
    "street": fake.street_name(),
    "postalCode": fake.postalcode(),
    "city": fake.city()
}


@pytest.fixture
def set_up_orders(clean_up_after_add_credit, create_product, product_data):
    customer_id = clean_up_after_add_credit
    _, product_id, bookstore_id = create_product
    new_product_data, _ = product_data
    products_data_for_order = [
        {
            "productId": product_id,
            "quantity": 1,
            "price": new_product_data["price"],
            "subTotal": new_product_data["price"]
        }
    ]
    utils_payments.add_credits_to_wallet(customer_id, 200.00)

    response, response_data = utils_orders.create_purchase_order(customer_id, bookstore_id, products_data_for_order, address_data)
    order_id = response_data["orderId"]
    print(f"Order ID: {order_id}")
    yield response, response_data
    # utils_main.remove_items_in_db(schema_for_db_order_order_items, order_id, db_column="order_id")
    # utils_main.remove_items_in_db(schema_for_db_order_order_address, order_id, db_column="order_id")
    # utils_main.remove_items_in_db(schema_for_db_order_orders, order_id)
    # utils_main.remove_items_in_db(schema_for_db_payment_payments, order_id, db_column="order_id")

