from  config.bd import bd,app,ma

class Banner(bd.model):
    __tablename__='tblBanner'
    id = bd.Column(bd.Integer, primary_key = True)
    titulo = bd.Column(bd.String(50))
    descripcion = bd.Column(bd.String(50))
    fecha = bd.Column(bd.String(50))
    def __init__(self,titulo,descripcion,fecha):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha

with app.app_context():
 bd.create_all()

class BannerSchema(ma.Schema):
    class Meta:
        fields=("id","titulo","descripcion","fecha")    