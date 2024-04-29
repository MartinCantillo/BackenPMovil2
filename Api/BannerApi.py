from flask import Flask, Blueprint, request, jsonify
from config.bd import app, bd, ma
from Models.Banner import Banner, BannerSchema

ruta_banner = Blueprint("route_Banner", __name__)

Banner_schema = BannerSchema()
Banners_schema = BannerSchema(many=True)

@ruta_banner.route("/saveBanner", methods=['POST'])
def saveBanner():
    titulo= request.json['titulo']
    descripcion = request.json['descripcion']
    fecha = request.json['fecha']
    newBanner = Banner(titulo, descripcion,fecha)
    bd.session.add(newBanner)
    bd.session.commit()
    return "saved"


@ruta_banner.route("/GetAllBanners", methods=["GET"])
def GetAll():
    resultAll = Banner.query.all()
    respo = Banners_schema(resultAll)
    return jsonify(respo)


@ruta_banner.route("deleteBanner", methods=['DELETE'])
def deleteBanner():
    id = request.json['id'] 
    banner = Banner.query.get(id)    
    if banner:
        bd.session.delete(banner)
        bd.session.commit()     
        return jsonify(Banner_schema.dump(banner))
    else: 
         return jsonify({"message": "Banner not found"}), 404 


@ruta_banner.route("/updateBanner", methods=['POST'])
def updateBanner():    
    id = request.json['id'] 
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    fecha = request.json['fecha']
    bannerGot = Banner.query.get(id)  
    if bannerGot:
        bannerGot.username = titulo
        bannerGot.descripcion = descripcion
        bannerGot.fecha = fecha
        bd.session.commit()     
        return "Updated sussefull"
    else: 
         return jsonify({"message": "Banner not found"}), 404 