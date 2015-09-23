__author__ = 'mika'

from app import db
from sqlalchemy.dialects.postgresql import JSON


class Result(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String, primary_key=True)
    password = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, id, password, email):
        self.id = id
        self.password = password
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)
