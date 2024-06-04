from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.Administrador import Administrador, AdministradorSchema
from config.routeProtection import token_required

ruta_admin = Blueprint("route_Administrador", __name__)

admin_schema = AdministradorSchema()
admins_schema = AdministradorSchema(many=True)

@ruta_admin.route("/saveAdmin", methods=['POST'])
@token_required
def saveAdmin():
    nombreAdmin= request.json['nombreAdmin']
    apellidoAdmin = request.json['apellidoAdmin']
    telefono = request.json['telefono']
    newAdmin = Administrador(nombreAdmin, apellidoAdmin,telefono)
    bd.session.add(newAdmin)
    bd.session.commit()
    return "saved"


@ruta_admin.route("/GetAllAdmins", methods=["GET"])
@token_required
def GetAll():
    resultAll = Administrador.query.all()
    respo = admins_schema.dump(resultAll)
    return jsonify(respo)


@ruta_admin.route("/deleteAdmin", methods=['DELETE'])
@token_required
def deleteAdmin():
    id = request.json['id']
    admin = Administrador.query.get(id)
    if admin:
         bd.session.delete(admin)
         bd.session.commit()
         return jsonify(admin_schema.dump(admin))
    else:
         return jsonify({"message": "Admin not found"}), 404


@ruta_admin.route("/updateAdmin", methods=['POST'])
@token_required
def updateAdmin():
    id = request.json['id']
    nombreAdmin= request.json['nombreAdmin']
    apellidoAdmin = request.json['apellidoAdmin']
    telefono = request.json['telefono']
    adminGot = Administrador.query.get(id)
    if adminGot:
        adminGot.nombreAdmin = nombreAdmin
        adminGot.apellidoAdmin = apellidoAdmin
        adminGot.telefono = telefono
        bd.session.commit()
        return "Updated sussefull"
    else:
         return jsonify({"message": "Admin not found"}), 404