from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.User import User, UserSchema
from config.routeProtection import token_required

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


@app.route("/updateUser", methods=['POST'])
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
