from core import db
from .base import Model
from .relations import association


class Movie(Model, db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String(20))

    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    directing = db.relationship("Director", back_populates="movies")

    actors = db.relationship('Actor', secondary=association, lazy='subquery', backref='filmography', uselist=True)


    def __repr__(self):
        return '<Movie {}>'.format(self.name)