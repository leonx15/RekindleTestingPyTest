from utils import utils_main
import json

host = utils_main.load_config()["host_env"]


def add_credits_to_wallet(json_data):
    response = utils_main.make_api_request("POST", f"http://{host}:8182/api/v1/payments/credit", data=json_data)
    response_json = json.loads(response.text)
    return response, response_json


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
