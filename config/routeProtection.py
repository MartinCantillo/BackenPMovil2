from functools import wraps
from flask import jsonify, request
from config.Token import generate_token,verificate_token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        # Remover el prefijo 'Bearer ' del token
        if 'Bearer' in token:
            token = token.split(' ')[1]

        try:
            verificar_resultado = verificate_token(token)
            if verificar_resultado.get("error"):
                return jsonify({'message': verificar_resultado.get("mensaje")}), 401
        except:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(*args, **kwargs)

    return decorated
