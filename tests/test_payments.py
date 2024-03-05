from utils import utils_payments

class TestPayments:

    def test_add_credits(self, add_credits_to_user):
        credit_entry_id, customer_id = add_credits_to_user
        response, history_json = utils_payments.get_credit_history(customer_id)
        assert response.status_code == 200
        print(f"Response: {credit_entry_id}")
