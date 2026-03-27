class AccountAPI:

    def get_balance(self, token):
        if token != "fake-jwt-token-123":
            return {
                "status": "unauthorized",
                "balance": None
            }

        return {
            "status": "success",
            "balance": 1000.00
        }

    def get_transaction_history(self, token):
        if token != "fake-jwt-token-123":
            return {
                "status": "unauthorized",
                "transactions": []
            }

        return {
            "status": "success",
            "transactions": [
                {"type": "transfer", "amount": 200.00},
                {"type": "deposit", "amount": 500.00}
            ]
        }