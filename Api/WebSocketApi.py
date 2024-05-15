from flask_socketio import emit
from flask import Flask, Blueprint, request, jsonify

ruta_websocket = Blueprint("route_websocket", __name__)

#  WebSocket routes within the function
def configure_websocket_routes(socketio):
    @socketio.on('message')
    def handle_message(message):
        print('received message: ' + message)
        emit('response', {'data': 'This is a response from the server.'})
