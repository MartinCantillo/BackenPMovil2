from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.Administrador import Administrador, AdministradorSchema

ruta_user = Blueprint("route_Administrador", __name__)

admin_schema = AdministradorSchema()
admins_schema = AdministradorSchema(many=True)

@ruta_user.route("/saveAdmin", methods=['POST'])
def saveAdmin():
    nombreAdmin= request.json['nombreAdmin']
    apellidoAdmin = request.json['apellidoAdmin']
    telefono = request.json['telefono']
    newAdmin = Administrador(nombreAdmin, apellidoAdmin,telefono)
    bd.session.add(newAdmin)
    bd.session.commit()
    return "saved"


@ruta_user.route("/GetAllAdmins", methods=["GET"])
def GetAll():
    resultAll = Administrador.query.all()
    respo = admins_schema(resultAll)
    return jsonify(respo)


@ruta_user.route("deleteAdmin", methods=['DELETE'])
def deleteUser():
    id = request.json['id'] 
    admin = Administrador.query.get(id)    
    bd.session.delete(admin)
    bd.session.commit()     
    return jsonify(admin_schema.dump(admin))


@app.route("/updateAdmin", methods=['POST'])
def updateUser():    
    id = request.json['id'] 
    nombreAdmin= request.json['nombreAdmin']
    apellidoAdmin = request.json['apellidoAdmin']
    telefono = request.json['telefono']
    adminGot = Administrador.query.get(id)  
    adminGot.nombreAdmin = nombreAdmin
    adminGot.apellidoAdmin = apellidoAdmin
    adminGot.telefono = telefono
    bd.session.commit()     
    return "Updated sussefull"