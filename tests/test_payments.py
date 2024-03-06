from utils import utils_payments


class TestPayments:

    def test_add_credits(self, set_up_to_add_credit):
        customer_id = set_up_to_add_credit
        utils_payments.add_credits_to_wallet(customer_id, 100)
        utils_payments.add_credits_to_wallet(customer_id, 101)
        utils_payments.add_credits_to_wallet(customer_id, 102)
        response, history_json = utils_payments.get_credit_history(customer_id)
        assert response.status_code == 200
        total_values = utils_payments.count_credit_amount(history_json)
        print(f"Credit entry ID: , totals: {total_values}")
