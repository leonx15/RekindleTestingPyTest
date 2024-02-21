from utils import get_jwt_token as jwt_token
from utils import load_config
import requests


class TestBookstores:
    def test_api_status(self):
        host = load_config()["host_env"]
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        response = requests.get(f"http://{host}:8183/api/v1/bookstores", headers=headers)
        assert response.status_code == 200

    def test_text_in_response(self):
        host = load_config()["host_env"]
        headers = {
            "Authorization": f"Bearer {jwt_token}"
        }
        response = requests.get(f"http://{host}:8183/api/v1/bookstores", headers=headers)
        expected_string = "\"isActive\":false"
        assert expected_string in response.text, "Expected text found."
