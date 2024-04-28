from  config.bd import bd,app,ma

class User(bd.model):
    __tablename__='tblUser'
    id = bd.Column(bd.Integer, primary_key = True)
    username = bd.Column(bd.String(50))
    password = bd.Column(bd.String(50))
    def __init__(self,username,password):
        self.username = username
        self.password = password

with app.app_context():
    bd.create_all()

class UserSchema(ma.Schema):
    class Meta:
        fields=("id","username","password")    