from utils import utils_orders, utils_payments

class TestOrders:

    def test_create_purchase_order(self, set_up_orders):
        response, response_data = set_up_orders
        assert response_data["message"] == "Order created successfully"
        print(f"Order data: {response_data} in {response}")
