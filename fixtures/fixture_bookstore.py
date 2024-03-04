import pytest
from utils import utils_bookstores, utils_main

schema_for_db_bookstores = "bookstore.bookstores"
schema_for_db_items = "bookstore.products"
schema_for_db_bookstore_items = "bookstore.bookstore_products"


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


def item_data_in_bookstore():
    new_item_data = {
        "name": "TestItem",
        "price": 100,
        "available": True
    }
    updated_item_data = {
        "name": "UpdatedItem",
        "price": 10,
        "available": True
    }
    return new_item_data, updated_item_data


@pytest.fixture()
def create_bookstore(bookstore_data):
    response, bookstore_id = utils_bookstores.create_bookstore(bookstore_data[0])
    yield response, bookstore_id
    utils_main.remove_items_in_db(schema_for_db_bookstores, bookstore_id)
    print("Bookstore destroyed.")

@pytest.fixture
def create_item_for_bookstore(create_bookstore):
    _, bookstore_id = create_bookstore
    response, item_id, *trash = utils_bookstores.add_item_to_bookstore(bookstore_id, item_data_in_bookstore()[0])
    yield response, item_id, bookstore_id
    utils_main.remove_items_in_db(schema_for_db_bookstore_items, bookstore_id, "bookstore_id")
    print("Connection bookstore-item cleanup done.")
    utils_main.remove_items_in_db(schema_for_db_items, item_id)
    print(f"Item destroyed")