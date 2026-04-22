import random
import time


def generate_user():
    timestamp = int(time.time())
    random_part = random.randint(1000, 9999)
    return f"user_{timestamp}_{random_part}"


def generate_password():
    return "123456"


def generate_initial_balance():
    return 1000.0