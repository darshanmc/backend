from flask import Blueprint, jsonify, request, send_file
from ..models.user import User
from flask_cors import cross_origin
import zipfile
import csv
import io
import hashlib

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


@bp.route("/preview", methods=["POST"])
@cross_origin()
def preview():
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
            example: [["a", "b"], ["c", "d"]]
    responses:
      200:
        description: The same list of strings returned successfully
    """
    if not request.is_json:
        return jsonify({"error": "Invalid input"}), 400
    data = request.json
    if not isinstance(data, list) or not all(
        isinstance(sublist, list) and all(isinstance(item, str) for item in sublist)
        for sublist in data
    ):
        return (
            jsonify(
                {"error": "Invalid input format. Expected a list of lists of strings"}
            ),
            400,
        )

    return jsonify(hash_strings(data[0]))


@bp.route("/download", methods=["POST"])
@cross_origin()
def download():
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
            example: [["a", "b"], ["c", "d"]]
    responses:
      200:
        description: The same list of strings returned successfully
    """
    if not request.is_json:
        return jsonify({"error": "Invalid input"}), 400
    data = request.json
    if not isinstance(data, list) or not all(
        isinstance(sublist, list) and all(isinstance(item, str) for item in sublist)
        for sublist in data
    ):
        return (
            jsonify(
                {"error": "Invalid input format. Expected a list of lists of strings"}
            ),
            400,
        )

    # Create a zip file in memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for index, sublist in enumerate(data):
            # Create a CSV file in memory for each sublist
            csv_buffer = io.StringIO()
            csv_writer = csv.writer(csv_buffer)
            csv_writer.writerow(hash_strings(sublist))
            csv_buffer.seek(0)
            # Add the CSV file to the zip archive
            zip_file.writestr(f"data_{index + 1}.csv", csv_buffer.getvalue())
    zip_buffer.seek(0)

    return send_file(
        zip_buffer,
        mimetype="application/zip",
        as_attachment=True,
        download_name="data.zip",
    )


def hash_string(input_string):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Update the hash object with the bytes of the input string
    sha256_hash.update(input_string.encode("utf-8"))

    # Get the hexadecimal representation of the hash
    hex_digest = sha256_hash.hexdigest()

    return hex_digest


def hash_strings(strings):
    return [hash_string(string)[:6] for string in strings]
