from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.expert_system.rules import CocoaDiseaseDetector
from experta import Fact

api_bp = Blueprint("api", __name__)


@api_bp.route("/diagnose", methods=["POST"])
@jwt_required()
def diagnose():
    data = request.json
    print(data)

    # Convert string "true"/"false" to actual booleans
    for key, value in data.items():
        if isinstance(value, str):
            if value.lower() == "true":
                data[key] = True
            elif value.lower() == "false":
                data[key] = False

    engine = CocoaDiseaseDetector()
    engine.reset()

    # Declare facts
    for key, value in data.items():
        engine.declare(Fact(**{key: value}))

    engine.run()
    actions = [fact["action"] for fact in engine.facts.values() if "action" in fact]

    return jsonify({"actions": actions})


@api_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({"message": f"Hello user {current_user_id}"})


@api_bp.route("/diseases", methods=["GET"])
def diseases():
    return jsonify(
        {
            "diseases": [
                "Fusarium wilt",
                "Phytophthora rot",
                "Powdery mildew",
                "Leaf spot",
                "Damping-off",
                "Black pod disease",
                "Ceratocystis canker",
            ]
        }
    )
