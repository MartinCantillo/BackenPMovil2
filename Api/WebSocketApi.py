from flask_socketio import emit

#  WebSocket routes within the function
def configure_websocket_routes(socketio):
    @socketio.on('message')
    def handle_message(message):
        print('received message: ' + message)
        emit('response', {'data': 'This is a response from the server.'})
