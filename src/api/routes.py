"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token # type: ignore
from flask_jwt_extended import jwt_required, get_jwt_identity


api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
# create a user
@api.route('/create_user', methods=['POST'])
def create_user():
    request_body = request.get_json()
    email = request_body["email"]
    password = request_body["password"]
    user = User(email=email, password=password, is_active=True)
    db.session.add(user)
    
    db.session.commit()
    return jsonify({"message": "created_user"}), 200
# get all users
@api.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    users = list(map(lambda x: x.serialize(), users))
    return jsonify(users), 200
# create token
@api.route('/create_token', methods=['POST'])
def create_token():
    request_body = request.get_json()
    email = request_body["email"]
    password = request_body["password"]
    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"message": "invalid_credentials"}), 401
    access_token = create_access_token(identity=email)
    return jsonify({"token": access_token}), 200
