class AuthAPI:

    def login(self, username, password):
        if username == "" or password == "":
            return {
                "status": "required_fields",
                "message": "Username and password are required"
            }

        if username != "admin" or password != "1234":
            return {
                "status": "invalid_credentials",
                "message": "Invalid username or password"
            }

        return {
            "status": "success",
            "token": "fake-jwt-token-123"
        }