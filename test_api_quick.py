from api.account_api import AccountAPI

print("RESET:")
print(AccountAPI.reset_data())

print("\nBALANCE:")
print(AccountAPI.get_balance("mario_user"))

print("\nHISTORY:")
print(AccountAPI.get_history("mario_user"))

print("\nTRANSFER:")
print(AccountAPI.transfer("mario_user", 100))

print("\nBALANCE AFTER TRANSFER:")
print(AccountAPI.get_balance("mario_user"))