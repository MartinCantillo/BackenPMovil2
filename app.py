from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from config.bd import app
from Api.UserApi import ruta_user
from Api.BannerApi import ruta_banner
from Api.AdministradorApi import ruta_admin
from Api.ResidenteApi import ruta_residente
from Api.AnomaliaApi import ruta_anomalia
from Api.WebSocketApi import configure_websocket_routes  # Import the function

# Import the  Blueprints
app.register_blueprint(ruta_user, url_prefix="/api")
app.register_blueprint(ruta_banner, url_prefix="/api")
app.register_blueprint(ruta_admin, url_prefix="/api")
app.register_blueprint(ruta_residente, url_prefix="/api")
app.register_blueprint(ruta_anomalia, url_prefix="/api")

@app.route("/")
def index():
    return "Welcome"

#Enable CORS for the entire application
CORS(app)

# Initialize Flask app and SocketIO
socketio = SocketIO(app, cors_allowed_origins="*") 

# Configure WebSocket routes
configure_websocket_routes(socketio)

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5000, host="0.0.0.0")
