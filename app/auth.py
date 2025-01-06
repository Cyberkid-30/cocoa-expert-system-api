from flask import Blueprint, request, jsonify
from app.models import User, db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    # Parse the request data
    data = request.get_json()
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid input. JSON data required."}), 400

    # Extract username and password
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Both username and password are required."}), 400

    # Query the user from the database
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials."}), 401

    # Create the JWT token using a string for the identity
    access_token = create_access_token(
        identity=str(user.id)
    )  # Ensure identity is a string

    return jsonify({"access_token": access_token}), 200
