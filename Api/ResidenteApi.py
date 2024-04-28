from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.Residente import Residente, ResidenteSchema

ruta_user = Blueprint("route_Residente", __name__)

Residente_schema = ResidenteSchema()
Residentes_schema = ResidenteSchema(many=True)

@ruta_user.route("/saveResidente", methods=['POST'])
def saveResidente():
    nombreResidente= request.json['nombreResidente']
    apellidoResidente = request.json['apellidoResidente']
    numApartamento= request.json['numApartamento']
    numTelefono = request.json['numTelefono']
    IdUser = request.json['IdUser']
    newResidente = Residente(nombreResidente, apellidoResidente,numApartamento,numTelefono,IdUser)
    bd.session.add(newResidente)
    bd.session.commit()
    return "saved"


@ruta_user.route("/GetAllresidentes", methods=["GET"])
def GetAll():
    resultAll = Residente.query.all()
    respo = Residentes_schema(resultAll)
    return jsonify(respo)


@ruta_user.route("deleteResidente", methods=['DELETE'])
def deleteResidente():
    id = request.json['id'] 
    residente = Residente.query.get(id)
    if residente:        
        bd.session.delete(residente)
        bd.session.commit()     
        return jsonify(Residente_schema.dump(residente))
    else:
         return jsonify({"message": "Residente not found"}), 404 


@app.route("/updateResidente", methods=['POST'])
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

@ruta_user.route("/GetResidenteById", methods=["GET"])
def GetResidenteById(id):
    residente = request.json['id'] 
    if residente:
        return Residente_schema.jsonify(residente)
    else:
        return jsonify({"message": "Residente not found"}), 404
