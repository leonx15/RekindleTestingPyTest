from utils import utils_main
from utils import utils_bookstores
from fixtures.fixture_bookstore import create_bookstore, bookstore_data, create_product, product_data

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

    def test_create_product(self, create_product):
        response, product_id, *trash = create_product
        print(f"Response: {response}")
        assert response.status_code == 201

    def test_get_product_info(self, create_product, product_data):
        new_product_data, _ = product_data
        _, product_id, bookstore_where_product_added = create_product
        product_data_from_api = utils_bookstores.get_product_data(product_id)
        print(f"Product data from API: {product_data_from_api}")
        assert new_product_data['name'] == product_data_from_api['name']
        assert new_product_data['price'] == product_data_from_api['price']
        assert new_product_data['available'] == product_data_from_api['available']
        assert bookstore_where_product_added in product_data_from_api['bookstores']

    def test_update_product_info(self, create_product, product_data):
        _, updated_product_data = product_data
        _, product_id, bookstore_where_product_added = create_product
        response = utils_bookstores.update_product_data(product_id, updated_product_data)
        assert response.status_code == 204
        product_data_from_api = utils_bookstores.get_product_data(product_id)
        assert updated_product_data['name'] == product_data_from_api['name']
        assert updated_product_data['price'] == product_data_from_api['price']
        assert updated_product_data['available'] == product_data_from_api['available']
        assert bookstore_where_product_added in product_data_from_api['bookstores']
