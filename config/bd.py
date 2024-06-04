from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/bdmovil2'
user = "Georgx12"
password = "Ul120702"
direc = "Georgx12.mysql.pythonanywhere-services.com"
namebd = "Georgx12$residentul"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{direc}/{namebd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Movil2"

bd = SQLAlchemy(app)
ma = Marshmallow(app)