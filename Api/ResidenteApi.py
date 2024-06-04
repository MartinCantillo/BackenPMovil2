from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.Residente import Residente, ResidenteSchema
from config.routeProtection import token_required

ruta_residente = Blueprint("route_Residente", __name__)

Residente_schema = ResidenteSchema()
Residentes_schema = ResidenteSchema(many=True)

@ruta_residente.route("/saveResidente", methods=['POST'])
def saveResidente():
    nombreResidente = request.json['nombreResidente']
    apellidoResidente = request.json['apellidoResidente']
    numApartamento = request.json['numApartamento']
    numTelefono = request.json['numTelefono']
    idUser = request.json['idUser']

    newResidente = Residente(nombreResidente, apellidoResidente, numApartamento, numTelefono, idUser)
    bd.session.add(newResidente)
    bd.session.commit()

    residente_id = newResidente.id

    return jsonify({'message': 'Residente saved', 'residente_id': residente_id}), 200


@ruta_residente.route("/GetAllresidentes", methods=["GET"])
@token_required
def GetAll():
    resultAll = Residente.query.all()
    respo = Residentes_schema.dump(resultAll)
    return jsonify(respo)


@ruta_residente.route("/deleteResidente", methods=['DELETE'])
@token_required
def deleteResidente():
    id = request.json['id']
    residente = Residente.query.get(id)
    if residente:
        bd.session.delete(residente)
        bd.session.commit()
        return jsonify(Residente_schema(residente))
    else:
         return jsonify({"message": "Residente not found"}), 404


@ruta_residente.route("/updateResidente", methods=['POST'])
@token_required
def updateResidente():
    id = request.json['id']
    nombreResidente= request.json['nombreResidente']
    apellidoResidente = request.json['apellidoResidente']
    numApartamento= request.json['numApartamento']
    numTelefono = request.json['numTelefono']
    IdUser = request.json['IdUser']
    residenteGot = Residente.query.get(id)
    if residenteGot:
        residenteGot.nombreResidente = nombreResidente
        residenteGot.apellidoResidente = apellidoResidente
        residenteGot.numApartamento = numApartamento
        residenteGot.numTelefono = numTelefono
        residenteGot.IdUser = IdUser
        bd.session.commit()
        return "Updated sussefull"
    else:
        return jsonify({"message": "Residente not found"}), 404

@ruta_residente.route("/GetResidenteById", methods=["POST"])
@token_required
def get_residente_by_id():
    id_usuario =request.json['IdUser']
    if not id_usuario:
        return jsonify({"message": "ID de usuario is required"}), 400

    residente = Residente.query.filter_by(IdUser=id_usuario).first()
    if residente:
        return jsonify(Residente_schema.dump(residente)),200
    else:
        return jsonify({"message": "Residente not found"}), 404
