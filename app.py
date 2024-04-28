from flask import Flask, request, redirect, render_template
from config.bd import app

#Rutas de las apis




@app.route("/")
def index():
    return "hola"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")