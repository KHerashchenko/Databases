from flask import Flask, request
from flask import current_app as app

from controllers.actor import *
from controllers.director import *
from controllers.movie import *


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/api/actors', methods=['GET'])
def actors():
    """
    Get all actors in db
    """
    return get_all_actors()


@app.route('/api/movies', methods=['GET'])
def movies():
    """
    Get all actors in db
    """
    return get_all_movies()

@app.route('/api/directors', methods=['GET'])
def directors():
    """
    Get all directors in db
    """
    return get_all_directors()

@app.route('/api/actor', methods=['GET', 'POST', 'PUT', 'DELETE'])
def actor():
    """
    GET: get actor by id
    POST: add new actor, body can include:
    name, gender, date_of_birth
    PUT: update actor, body can include:
    name, gender, date_of_birth
    DELETE: remove actor, body:
    id
    """
    if request.method == 'GET':
        return get_actor_by_id()
    if request.method == 'POST':
        return add_actor()
    if request.method == 'PUT':
        return update_actor()
    if request.method == 'DELETE':
        return delete_actor()


@app.route('/api/movie', methods=['GET', 'POST', 'PUT', 'DELETE'])
def movie():
    """
    GET: get movie by id
    POST: add new movie, body can include:
    name, year, genre
    PUT: update movie, body can include:
    name, year, genre
    DELETE: remove movie, body:
    id
    """
    if request.method == 'GET':
        return get_movie_by_id()
    if request.method == 'POST':
        return add_movie()
    if request.method == 'PUT':
        return update_movie()
    if request.method == 'DELETE':
        return delete_movie()


@app.route('/api/director', methods=['GET', 'POST', 'PUT', 'DELETE'])
def director():
    """
    GET: get director by id
    POST: add new director, body can include:
    name, gender, date_of_birth
    PUT: update director, body can include:
    name, gender, date_of_birth
    DELETE: remove director, body:
    id
    """
    if request.method == 'GET':
        return get_director_by_id()
    if request.method == 'POST':
        return add_director()
    if request.method == 'PUT':
        return update_director()
    if request.method == 'DELETE':
        return delete_director()


@app.route('/api/actor-relations', methods=['PUT', 'DELETE'])
def actor_relations():
    """
    PUT: add relations, body:
    id, relation_id
    DELETE: delete relations, body:
    id
    """
    if request.method == 'PUT':
        return actor_add_relation()
    if request.method == 'DELETE':
        return actor_clear_relations()


@app.route('/api/movie-relations', methods=['PUT', 'DELETE'])
def movie_relations():
    """
    PUT: add relations, body:
    id, relation_id
    DELETE: delete relations, body:
    id
    """
    if request.method == 'PUT':
        return movie_add_relation()
    if request.method == 'DELETE':
        return movie_clear_relations()