from utils import utils_main
from utils import utils_bookstores
import pytest

schema_for_db_bookstores = "bookstore.bookstores"


@pytest.fixture()
def bookstore_data():
    new_bookstore_data = {
        "name": "TestowaBooks",
        "isActive": True
    }
    bookstore_update_data = {
        "name": "UpdatedName",
        "isActive": False
    }
    return new_bookstore_data, bookstore_update_data


class TestBookstores:
    def test_api_status(self):
        response, _ = utils_bookstores.get_list_of_bookstores()
        assert response.status_code == 200

    def test_create_bookstore(self, bookstore_data):
        response, bookstore_id = utils_bookstores.create_bookstore(bookstore_data[0])
        assert response.status_code == 201
        _, bookstore_data = utils_bookstores.get_specific_bookstore(bookstore_id)
        assert bookstore_id == bookstore_data["id"]
        # Clean up
        utils_main.remove_items_in_db(schema_for_db_bookstores, bookstore_id)

    def test_update_bookstore(self, bookstore_data):
        _, bookstore_id = utils_bookstores.create_bookstore(bookstore_data[0])
        response = utils_bookstores.update_bookstore(bookstore_id, bookstore_data[1])
        assert response.status_code == 204
        _, updated_bookstore_data = utils_bookstores.get_specific_bookstore(bookstore_id)
        assert bookstore_id == updated_bookstore_data["id"]
        assert updated_bookstore_data["name"] == bookstore_data[1]["name"]
        assert updated_bookstore_data["isActive"] == bookstore_data[1]["isActive"]
        # Clean up
        utils_main.remove_items_in_db(schema_for_db_bookstores, bookstore_id)

    def test_delete_bookstore(self, bookstore_data):
        _, bookstore_id = utils_bookstores.create_bookstore(bookstore_data[0])
        _, created_bookstore_data = utils_bookstores.get_specific_bookstore(bookstore_id)
        assert created_bookstore_data["id"] == bookstore_id
        utils_bookstores.delete_bookstore(bookstore_id)
        response, _ = utils_bookstores.get_specific_bookstore(bookstore_id, allowed_statuses=[404])
        assert response.status_code == 404
        # Clean up
        utils_main.remove_items_in_db(schema_for_db_bookstores, bookstore_id)
