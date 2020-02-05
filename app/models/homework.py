from app.extension import db

class HomeworkModel(db.Model):
    __tablename__ = 'homeworks'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    homework_1_deadline = db.Column(db.DateTime)
    homework_2_deadline = db.Column(db.DateTime)
    homework_3_deadline = db.Column(db.DateTime)
    homework_4_deadline = db.Column(db.DateTime)
    homework_title = db.Column(db.String)
    homework_description = db.Column(db.String)
    homework_type = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)