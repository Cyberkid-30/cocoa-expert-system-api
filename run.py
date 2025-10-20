from app import create_app
from flask import jsonify
import os

app = create_app()


@app.route("/", methods=["GET"])  # type: ignore
def home():
    return jsonify({"message": "Welcome to the Cocoa Expert System API"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
