from utils import utils_orders

class TestOrders:

    def test_create_purchase_order(self, create_new_customer, create_product):
        _, customer_id = create_new_customer
        _, product_id, bookstore_id = create_product
        product_data = [
            {
                # "productId": product_id,
                "quantity": 1,
                "price": 20,
                "subTotal": 20
            }
        ]
        address_data = {
            "street": "TestowaUlica",
            "postalCode": "123-45",
            "city": "BigCity"
        }
        order_data = utils_orders.create_purchase_order(customer_id, bookstore_id, product_data, address_data)
        print(f"Order data: {order_data}")
        assert 2 == 1+1