from flask import jsonify, make_response
from datetime import datetime as dt

from models import Actor, Movie
from settings.constants import ACTOR_FIELDS  # to make response pretty
from controllers.parse_request import get_request_data


def get_all_actors():
    """
    Get list of all records
    """
    all_actors = Actor.query.all()
    actors = []
    for actor in all_actors:
        act = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        try:
            act['date_of_birth'] = (act['date_of_birth']).strftime("%Y-%m-%d")
        except:
            pass
        actors.append(act)
    return make_response(jsonify(actors), 200)


def get_actor_by_id():
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

        obj = Actor.query.filter_by(id=row_id).first()
        try:
            actor = {k: v for k, v in obj.__dict__.items() if k in ACTOR_FIELDS}
        except:
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        return make_response(jsonify(actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)

def add_actor():
    """
    Add new actor
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

    if Actor.query.filter_by(name=data_to_add['name']).first():
        err = 'Record with such name already exists'
        return make_response(jsonify(error=err), 400)
    new_record = Actor.create(**data_to_add)
    new_actor = {k: v for k, v in new_record.__dict__.items() if k in ACTOR_FIELDS}
    return make_response(jsonify(new_actor), 200)



def update_actor():
    """
    Update actor record by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Actor.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        data_actor_upd = {}
        if 'name' in data.keys():
            try:
                data_actor_upd['name'] = str(data['name'])
            except:
                err = 'Name must be string'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No name specified'
            return make_response(jsonify(error=err), 400)

        if 'date_of_birth' in data.keys():
            try:
                data_actor_upd['date_of_birth'] = dt.strptime(data['date_of_birth'], '%Y-%m-%d').date()
            except:
                err = 'Date of birth must be of format %Y-%m-%d'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No date specified'
            return make_response(jsonify(error=err), 400)

        if 'gender' in data.keys():
            try:
                data_actor_upd['gender'] = str(data['gender'])
            except:
                err = 'Gender of birth must be string'
                return make_response(jsonify(error=err), 400)
        else:
            err = 'No gender specified'
            return make_response(jsonify(error=err), 400)

        upd_record = Actor.update(row_id, **data_actor_upd)
        upd_actor = {k: v for k, v in upd_record.__dict__.items() if k in ACTOR_FIELDS}
        return make_response(jsonify(upd_actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def delete_actor():
    """
    Delete actor by id
    """
    data = get_request_data()
    if 'id' in data.keys():
        try:
            row_id = int(data['id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        if not Actor.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        del_actor = Actor.delete(row_id)
        msg = 'Record successfully deleted'
        return make_response(jsonify(message=msg), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)


def actor_add_relation():
    """
    Add a movie to actor's filmography
    """
    data = get_request_data()
    if 'id' in data.keys() and 'relation_id' in data.keys():
        try:
            actor_id = int(data['id'])
            movie_id = int(data['relation_id'])
        except:
            err = 'Id must be integer'
            return make_response(jsonify(error=err), 400)

        try:
            movie = Movie.query.filter_by(id=movie_id).first()
        except:
            err = 'Movie record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        if not Actor.query.filter_by(id=actor_id).first():
            err = 'Actor record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        actor = Actor.add_relation(1, movie)
        rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        rel_actor['filmography'] = str(actor.filmography)
        return make_response(jsonify(rel_actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)



def actor_clear_relations():
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

        if not Actor.query.filter_by(id=row_id).first():
            err = 'Record with such id does not exist'
            return make_response(jsonify(error=err), 400)

        actor = Actor.clear_relations(row_id)
        rel_actor = {k: v for k, v in actor.__dict__.items() if k in ACTOR_FIELDS}
        rel_actor['filmography'] = str(actor.filmography)
        return make_response(jsonify(rel_actor), 200)

    else:
        err = 'No id specified'
        return make_response(jsonify(error=err), 400)
