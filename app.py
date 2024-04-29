from flask import Flask, request, redirect, render_template
from config.bd import app

#Routes of the  apis
from Api.UserApi import ruta_user
from Api.BannerApi import ruta_banner
from Api.AdministradorApi import ruta_admin
from Api.ResidenteApi import ruta_residente
from Api.AnomaliaApi import ruta_anomalia

# Import the  Blueprints
app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_banner, url_prefix="/api")
app.register_blueprint(ruta_admin, url_prefix="/api")
app.register_blueprint(ruta_residente, url_prefix="/api")
app.register_blueprint(ruta_anomalia, url_prefix="/api")

@app.route("/")
def index():
    return "Welcome"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")