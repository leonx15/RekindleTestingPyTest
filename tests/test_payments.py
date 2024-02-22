from utils import utils_main
import requests


class TestPayments:
    def test_api_status(self):
        host = utils_main.load_config()["host_env"]
        order_id = "idOfOrder"
        headers = {
            "Authorization": f"Bearer {utils_main.get_jwt_token()}"
        }
        response = requests.get(f"http://{host}:8182/api/v1/payments/{order_id}", headers=headers)
        assert response.status_code == 200
