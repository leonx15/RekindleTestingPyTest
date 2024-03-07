from utils import utils_main, utils_customers, utils_bookstores, utils_payments
import json

host = utils_main.load_config()["host_env"]


def create_purchase_order(customer_id, bookstore_id, product_data, address_data):
    request_data = {
        "customerId": customer_id,
        "bookstoreId": bookstore_id,
        "price": 0,
        "items": product_data,
        "address": address_data
    }
    # response = utils_main.make_api_request("POST", f"http://{host}:8181/api/v1/orders", data=request_data)
    # response_data = json.loads(response.text)
    return request_data
