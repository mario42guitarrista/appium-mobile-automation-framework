from pages.base_page import BasePage


class MenuPage(BasePage):

    def get_transaction_history(self):
        # simulação
        return [
            {"type": "transfer", "amount": 200},
            {"type": "deposit", "amount": 500}
        ]