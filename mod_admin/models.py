from leaderboard import db
from sqlalchemy.ext.hybrid import hybrid_property

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "{}".format(self.email)