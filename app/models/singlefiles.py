from app.extension import db

class SinglefileModel(db.Model):
    __tablename__ = 'singlefiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    homework_id = db.Column(db.Integer)
    source = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    late = db.Column(db.Boolean)
    file_name = db.Column(db.String)