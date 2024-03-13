from utils import utils_payments


class TestPayments:

    def test_add_credits(self, clean_up_after_add_credit):
        customer_id = clean_up_after_add_credit
        amount_total = 0
        amounts = [100.5, 101, 102, 103]
        for amount in amounts:
            utils_payments.add_credits_to_wallet(customer_id, amount)
            amount_total += amount
        response, history_json = utils_payments.get_credit_history(customer_id)
        assert response.status_code == 200
        total_credits_from_history = utils_payments.count_credit_amount(history_json)
        assert amount_total == total_credits_from_history
        print(f"Customer ID: {customer_id}, totals from history: {total_credits_from_history} and added by test: {amount_total}")
