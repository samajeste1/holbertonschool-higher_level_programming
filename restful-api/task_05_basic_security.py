#!/usr/bin/python3
"""task_05_basic_security

Provides:
- /basic-protected  (Basic Auth)
- /login            (POST -> returns JWT)
- /jwt-protected    (Requires JWT)
- /admin-only       (Requires JWT and admin role)
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-for-demo"  # replace in prod
jwt = JWTManager(app)
auth = HTTPBasicAuth()

# in-memory user store
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return False
    return check_password_hash(user["password"], password)


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 400
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        return jsonify({"error": "Missing credentials"}), 400
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad credentials"}), 401
    additional_claims = {"role": user.get("role")}
    access_token = create_access_token(identity=username, additional_claims=additional_claims)
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    claims = get_jwt()
    role = claims.get("role")
    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# JWT error handlers to always return 401 for token problems (required by checker)
@jwt.unauthorized_loader
def custom_unauthorized_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def custom_invalid_token_callback(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def custom_expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run()
