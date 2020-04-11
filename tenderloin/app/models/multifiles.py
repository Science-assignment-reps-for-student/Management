from tenderloin.app.extension import db


class MultifileModel(db.Model):
    __tablename__ = "multi_files"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer)
    homework_id = db.Column(db.Integer)
    source = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    late = db.Column(db.Boolean)
    file_name = db.Column(db.String)
