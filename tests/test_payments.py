from utils import utils_payments


class TestPayments:

    def test_add_credits(self, add_credits_to_customer, data_to_add_credits):
        credit_entry_id, customer_id = add_credits_to_customer
        response, history_json = utils_payments.get_credit_history(customer_id)
        assert response.status_code == 200
        total_values = utils_payments.count_credit_amount(history_json)
        assert total_values == data_to_add_credits['totalPrice']
        print(f"Response: {credit_entry_id}, totals: {total_values}")
