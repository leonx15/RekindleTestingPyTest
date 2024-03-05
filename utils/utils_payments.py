from utils import utils_main
import json

host = utils_main.load_config()["host_env"]

def add_credits_to_wallet(json_data):
    response = utils_main.make_api_request("POST", f"http://{host}:8182/api/v1/payments/credit", data=json_data)
    credit_entry_id = json.loads(response.text)
    return response, credit_entry_id