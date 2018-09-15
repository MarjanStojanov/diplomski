from functools import wraps
from flask import request, abort, jsonify, render_template
from models import *
from schemas import *
from mit import db
from  mit import app
import json
import flask

def validate_token(validate_func):
    @wraps(validate_func)
    def validation_service(*args, **kwargs):
        token = api_token.query.filter(api_token.token==request.headers.get('MIT-API-TOKEN')).all()
        if not token:
            abort(401)
        return validate_func(*args, **kwargs)
    return validation_service



@app.route('/api/drzave', methods=['GET', 'POST'])
@validate_token
def vrati_drzave():
    if flask.request.method == 'GET':
        drzava_schema = DrzavaSchema(many=True)
        data = Drzava.query.all()
        result = drzava_schema.dump(data)
        return jsonify(result)

    elif flask.request.method == 'POST':
        pass# TODO: proveriti unete podatke i kreirati objekat
    else:
        return render_template('404.html'), 404





@app.route('/api/drzave/<int:ID>', methods=['GET', 'POST', 'PUT', 'DELETE'])
@validate_token
def vrati_drzavu(ID):
    if flask.request.method == 'GET':
        drzava_schema = DrzavaSchema()
        data = Drzava.query.filter(Drzava.id==ID).first()
        if data:
            result = drzava_schema.dump(data)
            return jsonify(result)
        else:
            return render_template('404.html'), 404

    elif flask.request.method == 'PUT':
        pass# TODO: proveriti unete podatke i kreirati objekat

    elif flask.request.method == 'POST':
        pass# TODO: proveriti unete podatke i kreirati objekat

    elif flask.request.method == 'DELETE':
        pass
    else:
        return render_template('404.html'), 404


@app.route('/api/drzave/<int:ID>/destinacije', methods=['GET', 'POST'])
@validate_token
def vrati_destinacije_drzave(ID):
    if flask.request.method == 'GET':
        data = Drzava.query.filter(drzava_id=id)
        return jsonify(data)
    elif flask.request.method == 'POST':
        pass# TODO: proveriti unete podatke i kreirati objekat
    else:
        return render_template('404.html'), 404



@app.route('/api/destinacije', methods=['GET', 'POST'])
@validate_token
def vrati_destinacije():
    if flask.request.method == 'GET':
        destinacija_schema = DestinacijaSchema(many=True)
        data = Destinacija.query.all()
        result = destinacija_schema.dump(data)
        return jsonify(result)

    elif flask.request.method == 'POST':
        pass# TODO: proveriti unete podatke i kreirati objekat
    else:
        return render_template('404.html'), 404


@app.route('/api/destinacije/<int:ID>', methods=['GET', 'PUT'])
@validate_token
def vrati_destinaciju(ID):
    if flask.request.method == 'GET':
        data = Drzava.query.all()
    elif flask.request.method == 'PUT':
        pass# TODO: proveriti unete podatke i kreirati objekat
    else:
        return render_template('404.html'), 404


@app.route('/api/admin/tokens', methods=['GET','PUT','POST'])
def token_manager():
    if flask.request.get('MIT-API-TOKEN') == 'secret_admin_token':
        token_schema = ApiTokenSchema(many=True)
        data = api_token.query.all()
        result = token_schema.dump(data)
        return result
    else:
        return 404
