#!/usr/bin/python3
"""task_04_flask

Simple Flask API with endpoints:
- /           -> welcome string
- /data       -> returns list of usernames
- /status     -> "OK"
- /users/<username> -> returns user object or {"error":"User not found"}
- /add_user   -> POST: add a user (json payload)
"""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# store users in memory as requested (no test data pushed to remote repo)
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # return list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    u = users.get(username)
    if u is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(u)


@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 400
    payload = request.get_json()
    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    # Build minimal user object (type keep as-is)
    user = {
        "username": username,
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    # debug False by default (safer for checkers)
    app.run()
