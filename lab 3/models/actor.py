from core import db
from .base import Model
from .relations import association


class Actor(Model, db.Model):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)

    movies = db.relationship('Movie', secondary=association, lazy='subquery', backref='cast', uselist=True)

    def __repr__(self):
        return '<Actor {}>'.format(self.name)