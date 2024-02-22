from utils import utils_main
import requests

def create_customer(host):
        headers = {
            "Authorization": f"Bearer {utils_main.get_jwt_token()}"
        }
        json_data = {
            "username": "Test1",
            "firstName": "Testiko",
            "lastName": "Testowy"
        }

        response = requests.post(f"http://{host}:8184/api/v1/customers", json=json_data, headers=headers)
        return response