import requests

url = "http://127.0.0.1:5000/login"

payload = {
    "username": "mario_user",
    "password": "123456"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())