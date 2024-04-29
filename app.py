from flask import Flask, request, redirect, render_template
from config.bd import app

#Routes of the  apis
from Api.UserApi import ruta_user
from Api.BannerApi import ruta_banner
from Api.AdministradorApi import ruta_admin
from Api.ResidenteApi import ruta_residente
from Api.AnomaliaApi import ruta_anomalia




@app.route("/")
def index():
    return "Welcome"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")