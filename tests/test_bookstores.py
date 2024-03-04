from utils import utils_main
from utils import utils_bookstores
from fixtures.fixture_bookstore import create_bookstore, bookstore_data, create_product_for_bookstore

schema_for_db_bookstores = "bookstore.bookstores"
schema_for_db_items = "bookstore.products"
schema_for_db_bookstore_items = "bookstore.bookstore_products"


class TestBookstores:
    def test_api_status(self):
        response, _ = utils_bookstores.get_list_of_bookstores()
        assert response.status_code == 200

    def test_create_bookstore(self, create_bookstore):
        response, bookstore_id = create_bookstore
        assert response.status_code == 201
        _, specific_bookstore_data = utils_bookstores.get_specific_bookstore(bookstore_id)
        assert bookstore_id == specific_bookstore_data["id"]

    def test_update_bookstore(self, create_bookstore, bookstore_data):
        _, bookstore_id = create_bookstore
        response = utils_bookstores.update_bookstore(bookstore_id, bookstore_data[1])
        assert response.status_code == 204
        _, updated_bookstore_data = utils_bookstores.get_specific_bookstore(bookstore_id)
        assert bookstore_id == updated_bookstore_data["id"]
        assert updated_bookstore_data["name"] == bookstore_data[1]["name"]
        assert updated_bookstore_data["isActive"] == bookstore_data[1]["isActive"]

    def test_delete_bookstore(self, bookstore_data):
        _, bookstore_id = utils_bookstores.create_bookstore(bookstore_data[0])
        _, created_bookstore_data = utils_bookstores.get_specific_bookstore(bookstore_id)
        assert created_bookstore_data["id"] == bookstore_id
        utils_bookstores.delete_bookstore(bookstore_id)
        response, _ = utils_bookstores.get_specific_bookstore(bookstore_id, allowed_statuses=[404])
        assert response.status_code == 404, "Bookstore still exist."
        print("Bookstore successfully deleted.")


class TestBookstoreItems:

    def test_create_product(self, create_product_for_bookstore):
        response, product_id, *others = create_product_for_bookstore
        print(f"Response: {response}")
        assert response.status_code == 201


