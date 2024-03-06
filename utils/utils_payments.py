from utils import utils_main
import json

host = utils_main.load_config()["host_env"]


def add_credits_to_wallet(customer_id, amount):
    data_json = {
        "customerId": customer_id,
        "totalPrice": amount
    }
    response = utils_main.make_api_request("POST", f"http://{host}:8182/api/v1/payments/credit", data=data_json)
    credit_entry_id = json.loads(response.text)
    return response, credit_entry_id


def get_credit_history(customer_id):
    response = utils_main.make_api_request("GET", f"http://{host}:8182/api/v1/payments/credit/history/{customer_id}")
    response_json = json.loads(response.text)
    return response, response_json


def count_credit_amount(history_list):
    total_value = 0
    for entry in history_list:
        amount = entry.get('totalPrice', 0)
        if entry.get('transactionType') == "CREDIT":
            total_value += amount
        elif entry.get('transactionType') == "DEBIT":
            total_value -= amount
    return total_value
