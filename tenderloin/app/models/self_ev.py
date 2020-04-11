from tenderloin.app.extension import db


class SelfevaluationModel(db.Model):
    __tablename__ = "self_evaluations"

    id = db.Column(db.Integer, primary_key=True)
    scientific_accuracy = db.Column(db.Integer)
    communication = db.Column(db.Integer)
    attitude = db.Column(db.Integer)
    homework_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
