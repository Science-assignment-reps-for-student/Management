from app.extension import db

class MutualevaluationModel(db.Model):
    __tablename__ = 'mutual_evaluations'

    id = db.Column(db.Integer, primary_key=True)
    cooperation = db.Column(db.Integer)
    communication = db.Column(db.Integer)
    attitude = db.Column(db.Integer)
    homework_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    target_id = db.Column(db.Integer)