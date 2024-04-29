from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.Anomalia import Anomalia, AnomaliaSchema
from config.routeProtection import token_required

ruta_anomalia = Blueprint("route_Anomalia", __name__)

anomalia_schema = AnomaliaSchema()
anomalias_schema = AnomaliaSchema(many=True)

@ruta_anomalia.route("/saveAnomalia", methods=['POST'])
@token_required
def saveAnomalia():
    descripcionAnomalia= request.json['descripcionAnomalia']
    fechaReporteAnomalia = request.json['fechaReporteAnomalia']
    fotoAnomalia= request.json['fotoAnomalia']
    tipoAnomalia = request.json['tipoAnomalia']
    asuntoAnomalia= request.json['asuntoAnomalia']
    idEstadoAnomalia = request.json['idEstadoAnomalia']
    prioridad= request.json['prioridad']
    IdUser = request.json['IdUser']
    newAnomalia = Anomalia(descripcionAnomalia, fechaReporteAnomalia,fotoAnomalia,tipoAnomalia,asuntoAnomalia,idEstadoAnomalia,prioridad,IdUser)
    bd.session.add(newAnomalia)
    bd.session.commit()
    return "saved"


@ruta_anomalia.route("/GetAllAnomalias", methods=["GET"])
@token_required
def GetAll():
    resultAll = Anomalia.query.all()
    respo = anomalias_schema(resultAll)
    return jsonify(respo)


@ruta_anomalia.route("deleteAnomalia", methods=['DELETE'])
@token_required
def deleteAnomalia():
    id = request.json['id'] 
    anomalia = Anomalia.query.get(id)    
    if anomalia:
        bd.session.delete(anomalia)
        bd.session.commit()     
        return jsonify(anomalia_schema.dump(anomalia))
    else:
        return jsonify({"message": "Anomalia not found"}), 404 


@ruta_anomalia.route("/updateAnomalia", methods=['POST'])
@token_required
def updateAnomalia():    
    id = request.json['id'] 
    descripcionAnomalia= request.json['descripcionAnomalia']
    fechaReporteAnomalia = request.json['fechaReporteAnomalia']
    fotoAnomalia= request.json['fotoAnomalia']
    tipoAnomalia = request.json['tipoAnomalia']
    asuntoAnomalia= request.json['asuntoAnomalia']
    idEstadoAnomalia = request.json['idEstadoAnomalia']
    prioridad= request.json['prioridad']
    IdUser = request.json['IdUser']
    anomaliaGot = Anomalia.query.get(id)  
    if anomaliaGot:
        anomaliaGot.descripcionAnomalia = descripcionAnomalia
        anomaliaGot.fechaReporteAnomalia = fechaReporteAnomalia
        anomaliaGot.fotoAnomalia = fotoAnomalia
        anomaliaGot.tipoAnomalia = tipoAnomalia
        anomaliaGot.asuntoAnomalia = asuntoAnomalia
        anomaliaGot.idEstadoAnomalia = idEstadoAnomalia
        anomaliaGot.prioridad = prioridad
        anomaliaGot.IdUser = IdUser
        bd.session.commit()     
        return "Updated sussefull"
    else:
         return jsonify({"message": "Anomalia not found"}), 404 

@ruta_anomalia.route("/getAnomaliasByUserId", methods=['GET'])
@token_required
def getAnomaliasByUserId():
    idUser = request.json['idUser'] 
    anomalias = Anomalia.query.filter_by(IdUser=idUser).all()
    if anomalias:
        respo = anomalias_schema.dump(anomalias)
        return jsonify(respo)
    else:
        return jsonify({"message": "No anomalies found for user with id {}".format(idUser)}), 404 
