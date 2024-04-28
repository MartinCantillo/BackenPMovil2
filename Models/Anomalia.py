from  config.bd import bd,app,ma

class Anomalia(bd.model):
    __tablename__='tblAnomalia'
    id = bd.Column(bd.Integer, primary_key = True)
    descripcionAnomalia = bd.Column(bd.String(50))
    fechaReporteAnomalia = bd.Column(bd.String(50))
    fotoAnomalia = bd.Column(bd.String(50))
    tipoAnomalia = bd.Column(bd.String(50))
    asuntoAnomalia = bd.Column(bd.String(50))
    idEstadoAnomalia = bd.Column(bd.String(50))
    prioridad = bd.Column(bd.String(50))
    IdUser = bd.Column(bd.Integer, bd.ForeignKey("tblUser.id"))

    def __init__(self,descripcionAnomalia,fechaReporteAnomalia,fotoAnomalia,tipoAnomalia,asuntoAnomalia,idEstadoAnomalia,prioridad,IdUser):
        self.descripcionAnomalia = descripcionAnomalia
        self.fechaReporteAnomalia = fechaReporteAnomalia
        self.fotoAnomalia = fotoAnomalia
        self.tipoAnomalia = tipoAnomalia
        self.asuntoAnomalia = asuntoAnomalia
        self.idEstadoAnomalia=idEstadoAnomalia
        self.prioridad=prioridad
        self.IdUser=IdUser

with app.app_context():
    bd.create_all()

class AnomaliaSchema(ma.Schema):
    class Meta:
        fields=("id","descripcionAnomalia","fechaReporteAnomalia","fotoAnomalia","tipoAnomalia","asuntoAnomalia","idEstadoAnomalia","prioridad","IdUser")    