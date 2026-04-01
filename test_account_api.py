from api.auth_api import AuthAPI
from api.account_api import AccountAPI

print("LOGIN:")
print(AuthAPI.login("mario_user", "123456"))

print("\nBALANCE:")
print(AccountAPI.get_balance("mario_user"))

print("\nTRANSFER:")
print(AccountAPI.transfer("mario_user", 200))

print("\nHISTORY:")
print(AccountAPI.get_history("mario_user"))