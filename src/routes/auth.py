from flask import Blueprint, jsonify, request
from funtion_jwt import write_token, validate_token

auth_scope = Blueprint("auth_scope", __name__)

@auth_scope.route("login", methods=['POST'])
def login():
    data = request.get_json()
    if data.username == "gustavo":
        return write_token(data=request.get_json())
    else:
        response = jsonify({"message":"User not found"})
        response.status_code = 404
        return response
    
@auth_scope.route("/verify/token")
def verify():
    token = request.headers['Autorization'].split(" ")[1]
    return validate_token(token, output=True)