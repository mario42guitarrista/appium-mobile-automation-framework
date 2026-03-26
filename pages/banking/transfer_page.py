from pages.base_page import BasePage


class TransferPage(BasePage):

    def transfer(self, current_balance, amount):
        if amount <= 0:
            return {
                "status": "invalid_amount",
                "new_balance": current_balance
            }

        if amount > current_balance:
            return {
                "status": "insufficient_balance",
                "new_balance": current_balance
            }

        new_balance = current_balance - amount

        return {
            "status": "success",
            "new_balance": new_balance
        }