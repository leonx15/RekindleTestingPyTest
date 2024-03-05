from utils import utils_payments


class TestPayments:

    def test_add_credits(self, add_credits_to_customer):
        credit_entry_id, customer_id = add_credits_to_customer
        response, history_json = utils_payments.get_credit_history(customer_id)
        assert response.status_code == 200
        is_present = any(item.get('creditId') == credit_entry_id for item in history_json)
        print(f"Response: {credit_entry_id}")
