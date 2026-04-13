import copy
from flask import Flask, request, jsonify
from data import USERS, INITIAL_USERS

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    payload = request.get_json()
    username = payload.get("username")
    password = payload.get("password")

    user = USERS.get(username)

    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    if user["password"] != password:
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

    return jsonify({"status": "success", "message": "Login successful"}), 200


@app.route("/balance/<username>", methods=["GET"])
def get_balance(username):
    user = USERS.get(username)

    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    return jsonify({
        "status": "success",
        "balance": user["balance"]
    }), 200


@app.route("/transfer", methods=["POST"])
def transfer():
    payload = request.get_json()
    username = payload.get("username")
    amount = payload.get("amount")

    user = USERS.get(username)

    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    if amount <= 0:
        return jsonify({"status": "invalid_amount", "new_balance": user["balance"]}), 400

    if amount > user["balance"]:
        return jsonify({"status": "insufficient_balance", "new_balance": user["balance"]}), 400

    user["balance"] -= amount
    user["history"].append({"type": "transfer", "amount": amount})

    return jsonify({
        "status": "success",
        "new_balance": user["balance"]
    }), 200


@app.route("/history/<username>", methods=["GET"])
def history(username):
    user = USERS.get(username)

    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404

    return jsonify({
        "status": "success",
        "history": user["history"]
    }), 200


@app.route("/reset", methods=["POST"])
def reset_data():
    USERS.clear()
    USERS.update(copy.deepcopy(INITIAL_USERS))

    return jsonify({
        "status": "success",
        "message": "Mock data reset"
    }), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)