from pages.banking.transfer_page import TransferPage
from api.account_api import AccountAPI


class TransferService:
    def __init__(self, driver):
        self.transfer_page = TransferPage(driver)

    def transfer(self, initial_balance, amount):
        return self.transfer_page.transfer(initial_balance, amount)

    def transfer_with_insufficient_balance(self, current_balance, amount):
        return self.transfer_page.transfer(current_balance, amount)

    def transfer_invalid_amount(self, current_balance, amount):
        return self.transfer_page.transfer(current_balance, amount)

    def transfer_and_sync_api(self, username, initial_balance, amount):
        ui_result = self.transfer_page.transfer(initial_balance, amount)
        api_result = AccountAPI.transfer(username, amount)

        return {
            "ui_result": ui_result,
            "api_result": api_result
        }