from  config.bd import bd,app,ma

class Administrador(bd.model):
    __tablename__='tblAdministrador'
    id = bd.Column(bd.Integer, primary_key = True)
    nombreAdmin = bd.Column(bd.String(50))
    apellidoAdmin = bd.Column(bd.String(50))
    telefono = bd.Column(bd.String(50))

    def __init__(self,nombreAdmin,apellidoAdmin,telefono):
        self.nombreAdmin = nombreAdmin
        self.apellidoAdmin = apellidoAdmin
        self.telefono = telefono
        

with app.app_context():
    bd.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields=("id","nombreAdmin","apellidoAdmin","telefono")    