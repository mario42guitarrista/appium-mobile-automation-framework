from pages.base_page import BasePage


class HomePage(BasePage):

    def get_balance(self):
        # simulação inicial de saldo
        return 1000.00

    def is_balance_visible(self):
        return self.get_balance() is not None