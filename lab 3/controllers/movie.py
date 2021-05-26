from flask import jsonify, make_response

from ast import literal_eval

from models import Movie, Actor, Director
from settings.constants import MOVIE_FIELDS
from .parse_request import get_request_data


def get_all_movies():
    """
    Get list of all records
    """
    all_movies = Movie.query.all()
    movies = []
    for movie in all_movies:
        mov = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        movies.append(mov)
    return make_response(jsonify(movies), 200)

def get_movie_by_id():
    """
    Get record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        obj = Movie.query.filter_by(id=row_id).first()
        try:
            movie = {k: v for k, v in obj.__dict__.items() if k in MOVIE_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def add_movie():
    """
    Add new movie
    """
    data = get_request_data()
    data_to_add = {}

    if 'name' in data.keys():
        try:
            data_to_add['name'] = str(data['name'])
        except:
            err = 'Name must be string'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No name specified'
        return make_response(jsonify(error=err), 400)

    if 'year' in data.keys():
        try:
            data_to_add['year'] = int(data['year'])
        except:
            err = 'Year must be integer'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No year specified'
        return make_response(jsonify(error=err), 400)

    if 'genre' in data.keys():
        try:
            data_to_add['genre'] = str(data['genre'])
        except:
            err = 'Genre of birth must be string'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No genre specified'
        return make_response(jsonify(error=err), 400)

    if 'director_id' in data.keys():

        try:
            data_to_add['director_id'] = int(data['director_id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Director.query.filter_by(id=int(data['director_id'])).first():
            err = 'Director record with such id does not exist'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No director id specified'
        return make_response(jsonify(error=err), 400)

    if Movie.query.filter_by(name=data_to_add['name']).first():
        err = 'Record with such name already exists'
        return make_response(jsonify(error=err), 400)
    new_record = Movie.create(**data_to_add)
    new_actor = {k: v for k, v in new_record.__dict__.items() if k in MOVIE_FIELDS}
    return make_response(jsonify(new_actor), 200)

def update_movie():
    """
    Update movie record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Movie.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        data_movie_upd = {}
        if 'name' in data.keys():
            try:
                data_movie_upd['name'] = str(data['name'])
            except:
                err = 'Name must be string'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No name specified'
            return make_response(jsonify(error=err), 400)

        if 'year' in data.keys():
            try:
                data_movie_upd['year'] = int(data['year'])
            except:
                err = 'Year must be integer'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No year specified'
            return make_response(jsonify(error=err), 400)

        if 'genre' in data.keys():
            try:
                data_movie_upd['genre'] = str(data['genre'])
            except:
                err = 'Genre of birth must be string'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No genre specified'
            return make_response(jsonify(error=err), 400)

        if 'director_id' in data.keys():
            try:
                data_movie_upd['director_id'] = int(data['director_id'])
            except:
                err = 'Id must be integer'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No director id specified'
            return make_response(jsonify(error=err), 400)

        upd_record = Movie.update(row_id, **data_movie_upd)
        upd_actor = {k: v for k, v in upd_record.__dict__.items() if k in MOVIE_FIELDS}
        return make_response(jsonify(upd_actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def delete_movie():
    """
    Delete movie by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Movie.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        movie = Movie.clear_relations(row_id)
        del_movie = Movie.delete(row_id)

        msg = 'Record successfully deleted'
        return make_response(jsonify(message=msg), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def movie_add_relation():
    """
    Add actor to movie's cast
    """
    data = get_request_data()
    if 'id' in data.keys() and 'relation_id' in data.keys():
        try:
            actor_id = int(data['relation_id'])
            movie_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        try:
            actor = Actor.query.filter_by(id=actor_id).first()
        except:
            err = 'Actor record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        if not Movie.query.filter_by(id=movie_id).first():
            err = 'Movie record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        movie = Movie.add_relation(1, actor)
        rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        rel_movie['cast'] = str(movie.cast)
        return make_response(jsonify(rel_movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def movie_clear_relations():
    """
    Clear all relations by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Movie.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        movie = Movie.clear_relations(row_id)
        rel_movie = {k: v for k, v in movie.__dict__.items() if k in MOVIE_FIELDS}
        rel_movie['cast'] = str(movie.cast)
        return make_response(jsonify(rel_movie), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)