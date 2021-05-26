from flask import jsonify, make_response
from datetime import datetime as dt

from models import Director, Movie
from settings.constants import DIRECTOR_FIELDS  # to make response pretty
from controllers.parse_request import get_request_data


def get_all_directors():
    """
    Get list of all records
    """
    all_directors = Director.query.all()
    directors = []
    for director in all_directors:
        act = {k: v for k, v in director.__dict__.items() if k in DIRECTOR_FIELDS}
        try:
            act['date_of_birth'] = (act['date_of_birth']).strftime("%Y-%m-%d")
        except:
            pass
        directors.append(act)
    return make_response(jsonify(directors), 200)


def get_director_by_id():
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

        obj = Director.query.filter_by(id=row_id).first()
        try:
            director = {k: v for k, v in obj.__dict__.items() if k in DIRECTOR_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(director), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def add_director():
    """
    Add new director
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

    if 'date_of_birth' in data.keys():
        try:
            data_to_add['date_of_birth'] = dt.strptime(data['date_of_birth'], '%Y-%m-%d').date()
        except:
            err = 'Date of birth must be of format %Y-%m-%d'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No date specified'
        return make_response(jsonify(error=err), 400)

    if 'gender' in data.keys():
        try:
            data_to_add['gender'] = str(data['gender'])
        except:
            err = 'Gender of birth must be string'
            return make_response(jsonify(error=err), 400)
    else:
        err = 'No gender specified'
        return make_response(jsonify(error=err), 400)

    # use this for 200 response code
    if Director.query.filter_by(name=data_to_add['name']).first():
        err = 'Record with such name already exists'
        return make_response(jsonify(error=err), 400)
    new_record = Director.create(**data_to_add)
    new_director = {k: v for k, v in new_record.__dict__.items() if k in DIRECTOR_FIELDS}
    return make_response(jsonify(new_director), 200)



def update_director():
    """
    Update director record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Director.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        data_director_upd = {}
        if 'name' in data.keys():
            try:
                data_director_upd['name'] = str(data['name'])
            except:
                err = 'Name must be string'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No name specified'
            return make_response(jsonify(error=err), 400)

        if 'date_of_birth' in data.keys():
            try:
                data_director_upd['date_of_birth'] = dt.strptime(data['date_of_birth'], '%Y-%m-%d').date()
            except:
                err = 'Date of birth must be of format %Y-%m-%d'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No date specified'
            return make_response(jsonify(error=err), 400)

        if 'gender' in data.keys():
            try:
                data_director_upd['gender'] = str(data['gender'])
            except:
                err = 'Gender of birth must be string'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No gender specified'
            return make_response(jsonify(error=err), 400)

        upd_record = Director.update(row_id, **data_director_upd)
        upd_director = {k: v for k, v in upd_record.__dict__.items() if k in DIRECTOR_FIELDS}
        return make_response(jsonify(upd_director), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def delete_director():
    """
    Delete director by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Director.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        del_director = Director.delete(row_id)
        msg = 'Record successfully deleted'
        return make_response(jsonify(message=msg), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def director_add_relation():
    """
    Add a movie to director's filmography
    """
    data = get_request_data()
    if 'id' in data.keys() and 'relation_id' in data.keys():
        try:
            director_id = int(data['id'])
            movie_id = int(data['relation_id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        try:
            movie = Movie.query.filter_by(id=movie_id).first()
        except:
            err = 'Movie record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        if not Director.query.filter_by(id=director_id).first():
            err = 'Director record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        director = Director.add_relation(1, movie)
        rel_director = {k: v for k, v in director.__dict__.items() if k in DIRECTOR_FIELDS}
        rel_director['filmography'] = str(director.filmography)
        return make_response(jsonify(rel_director), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)



def director_clear_relations():
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

        if not Director.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        director = Director.clear_relations(row_id)
        rel_director = {k: v for k, v in director.__dict__.items() if k in DIRECTOR_FIELDS}
        rel_director['filmography'] = str(director.filmography)
        return make_response(jsonify(rel_director), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
