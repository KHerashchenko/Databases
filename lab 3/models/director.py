from core import db
from .base import Model


class Director(Model, db.Model):
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)

    movies = db.relationship("Movie", back_populates="directing")

    def __repr__(self):
        return '<Director {}>'.format(self.name)