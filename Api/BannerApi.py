from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.Banner import Banner, BannerSchema

ruta_user = Blueprint("route_Banner", __name__)

Banner_schema = BannerSchema()
Banners_schema = BannerSchema(many=True)

@ruta_user.route("/saveBanner", methods=['POST'])
def saveBanner():
    username= request.json['username']
    password = request.json['password']
    newuser = Banner(username, password)
    bd.session.add(newuser)
    bd.session.commit()
    return "saved"


@ruta_user.route("/GetAllBanners", methods=["GET"])
def GetAll():
    resultAll = Banner.query.all()
    respo = Banners_schema(resultAll)
    return jsonify(respo)


@ruta_user.route("deleteBanner", methods=['DELETE'])
def deleteBanner():
    id = request.json['id'] 
    banner = Banner.query.get(id)    
    bd.session.delete(banner)
    bd.session.commit()     
    return jsonify(Banner_schema.dump(banner))


@app.route("/updateBanner", methods=['POST'])
def updateBanner():    
    id = request.json['id'] 
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    fecha = request.json['fecha']
    bannerGot = Banner.query.get(id)  
    bannerGot.username = titulo
    bannerGot.descripcion = descripcion
    bannerGot.fecha = fecha
    bd.session.commit()     
    return "Updated sussefull"