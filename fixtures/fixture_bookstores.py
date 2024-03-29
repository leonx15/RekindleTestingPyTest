import pytest
from utils import utils_bookstores
from faker import Faker

schema_for_db_bookstores = "bookstore.bookstores"
schema_for_db_products = "bookstore.products"
schema_for_db_bookstore_products = "bookstore.bookstore_products"


@pytest.fixture()
def bookstore_data():
    fake = Faker()

    new_bookstore_data = {
        "name": fake.company() + "Books",
        "isActive": True
    }
    bookstore_update_data = {
        "name": fake.company() + " Books",
        "isActive": False
    }
    return new_bookstore_data, bookstore_update_data


@pytest.fixture()
def product_data():
    fake = Faker()

    new_item_data = {
        "name": fake.sentence(nb_words=3).rstrip('.'),
        "price": 100.05,
        "available": True
    }
    updated_item_data = {
        "name": fake.sentence(nb_words=3).rstrip('.'),
        "price": 10,
        "available": True
    }
    return new_item_data, updated_item_data


@pytest.fixture()
def create_bookstore(bookstore_data):
    response, bookstore_id = utils_bookstores.create_bookstore(bookstore_data[0])
    yield response, bookstore_id
    # utils_main.remove_items_in_db(schema_for_db_bookstores, bookstore_id)


@pytest.fixture()
def create_product(create_bookstore, product_data):
    _, bookstore_id = create_bookstore
    new_product_data, _ = product_data
    response, product_id, *trash = utils_bookstores.add_product_to_bookstore(bookstore_id, new_product_data)
    yield response, product_id, bookstore_id
    # utils_main.remove_items_in_db(schema_for_db_bookstore_products, bookstore_id, "bookstore_id")
    # utils_main.remove_items_in_db(schema_for_db_products, product_id)
