from utils import get_jwt_token as jwt_token
from utils import load_config
import requests


class TestPayments:
    def test_api_status(self):
        host = load_config()["host_env"]
        order_id = "idOfOrder"
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        response = requests.get(f"http://{host}:8182/api/v1/payments/{order_id}", headers=headers)
        assert response.status_code == 200
