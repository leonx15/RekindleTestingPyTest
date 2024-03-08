from utils import utils_orders, utils_payments

class TestOrders:

    def test_create_purchase_order(self, set_up_to_add_credit, create_product):
        customer_id = set_up_to_add_credit
        _, product_id, bookstore_id = create_product
        response, _ = utils_payments.add_credits_to_wallet(customer_id, 200)
        product_data = [
            {
                "productId": product_id,
                "quantity": 1,
                "price": 100,
                "subTotal": 100
            }
        ]
        address_data = {
            "street": "TestowaUlica",
            "postalCode": "123-45",
            "city": "BigCity"
        }
        response, response_data = utils_orders.create_purchase_order(customer_id, bookstore_id, product_data, address_data)
        print(f"Order data: {response_data} in {response}")
