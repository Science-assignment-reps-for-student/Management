from tenderloin.app.extension import db


class MemberModel(db.Model):
    __tablename__ = "members"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
