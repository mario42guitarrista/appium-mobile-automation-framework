import copy

INITIAL_USERS = {
    "mario_user": {
        "password": "123456",
        "balance": 1000.0,
        "history": [
            {"type": "deposit", "amount": 1500.0},
            {"type": "transfer", "amount": 500.0}
        ]
    }
}

USERS = copy.deepcopy(INITIAL_USERS)