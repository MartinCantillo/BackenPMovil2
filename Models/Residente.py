from  config.bd import bd,app,ma

class Residente(bd.Model):
    __tablename__='tblResidente'
    id = bd.Column(bd.Integer, primary_key = True)
    nombreResidente = bd.Column(bd.String(50))
    apellidoResidente = bd.Column(bd.String(50))
    numApartamento = bd.Column(bd.String(3))
    numTelefono = bd.Column(bd.String(10))
    IdUser = bd.Column(bd.Integer, bd.ForeignKey("tblUser.id"))

    def __init__(self,nombreResidente,apellidoResidente,numApartamento,numTelefono,IdUser):
        self.nombreResidente = nombreResidente
        self.apellidoResidente = apellidoResidente
        self.numApartamento = numApartamento
        self.numTelefono = numTelefono
        self.IdUser = IdUser

with app.app_context():
    bd.create_all()

class ResidenteSchema(ma.Schema):
    class Meta:
        fields=("id","nombreResidente","apellidoResidente","numApartamento","numTelefono","IdUser")