from app.extension import db

class TeamModel(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    leader_id = db.Column(db.Integer)
    homework_id = db.Column(db.Integer)
    team_name = db.Column(db.String)