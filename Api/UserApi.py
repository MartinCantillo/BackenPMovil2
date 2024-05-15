from flask import Flask, Blueprint, request, jsonify
from config.Token import generate_token
from config.bd import app, bd, ma
from Models.User import User, UserSchema
from config.routeProtection import token_required
from werkzeug.security import check_password_hash

ruta_user = Blueprint("route_user", __name__)

usuario_schema = UserSchema()
usuarios_schema = UserSchema(many=True)

@ruta_user.route("/saveUser", methods=['POST'])
def saveUser():
    username= request.json['username']
    password = request.json['password']
    newuser = User(username, password)
    bd.session.add(newuser)
    bd.session.commit()
    return "saved"


@ruta_user.route("/GetAllUsers", methods=["GET"])
@token_required
def GetAll():
    resultAll = User.query.all()
    respo = usuarios_schema(resultAll)
    return jsonify(respo)


@ruta_user.route("deleteUser", methods=['DELETE'])
@token_required
def deleteUser():
    id = request.json['id'] 
    usuario = User.query.get(id)    
    if usuario:
        bd.session.delete(usuario)
        bd.session.commit()     
        return jsonify(usuario_schema.dump(usuario))
    else:
        return jsonify({"message": "User not found"}), 404 


@ruta_user.route("/updateUser", methods=['POST'])
@token_required
def updateUser():    
    id = request.json['id'] 
    username = request.json['username']
    password = request.json['password']
    userGot = User.query.get(id)  
    if userGot:
        userGot.username = username
        userGot.password = password
        bd.session.commit()     
        return "Updated sussefull"
    else:
         return jsonify({"message": "User not found"}), 404 

@ruta_user.route("/login", methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "Invalid username or password"}), 401

    
    if user.password != password:
        return jsonify({"message": "Invalid username or password"}), 401

    # Generar token JWT
    token = generate_token(user.id, user.username)

    return jsonify({"token": token["token"]}), 200
