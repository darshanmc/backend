from flask import Blueprint, jsonify, request
from ..models.user import User
from flask_cors import cross_origin

bp = Blueprint("users", __name__)


@bp.route("/users", methods=["GET"])
@cross_origin()
def list_users():
    """
    List all users
        ---
    tags:
        - Users
    responses:
      200:
        description: List of users returned successfully
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@bp.route("/echo", methods=["POST"])
@cross_origin()
def echo_strings():
    """
    Echo a list of strings
        ---
    tags:
        - Users
    parameters:
        - in: body
          name: data
          description: List of strings to echo
          required: true
          schema:
            type: array
            items:
              type: string
              example: "hello"
    responses:
      200:
        description: The same list of strings returned successfully
    """
    if not request.is_json:
        return jsonify({"error": "Invalid input"}), 400
    data = request.json
    if not isinstance(data, list) or not all(isinstance(item, str) for item in data):
        return (
            jsonify({"error": "Invalid input format. Expected a list of strings"}),
            400,
        )
    return jsonify(data), 200
