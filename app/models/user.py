from app.extension import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String, unique=True)
    user_pw = db.Column(db.DateTime)
    user_number = db.Column(db.Integer, unique=True)
    user_name = db.Column(db.String)
    user_type = db.Column(db.Integer)