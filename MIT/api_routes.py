from functools import wraps
from flask import request, abort, jsonify, render_template, make_response
from sqlalchemy.sql.expression import func
from models import *
from schemas import *
from mit import db
from  mit import app
import json
import flask
def validate_token(validate_func):
    """
        dekorator za proveravanje tokena dodat na svim endpoint-ovima
    """
    @wraps(validate_func)
    def validation_service(*args, **kwargs):
        token = api_token.query.filter(api_token.token==request.headers.get('MIT-API-TOKEN')).all()
        if not token:
            return make_response(jsonify({'error':'authentication failed'})), 401

        return validate_func(*args, **kwargs)
    return validation_service



@app.route('/api/kontinenti', methods=['GET'])
@validate_token
def vrati_kontinente():
    """
        vrati sve kontinente
    """


    if flask.request.method == 'GET':
        kontinent_schema = KontinentSchema(many=True)
        data = Kontinent.query.all()
        if data:
            result = kontinent_schema.dump(data)
            return jsonify(result)
    else:
        err = flask.request.method + 'request not allowed'
        return make_response(jsonify({'error': err})), 405

@app.route('/api/kontinenti/<int:ID>/drzave', methods=['GET','POST'])
@validate_token
def vrati_drzave_kontinenta(ID):
    """
        vrati sve drzave kontinenta, ili dodaj drzavu na kontinent
    """
    if flask.request.method == 'GET':
        drzava_schema = DrzavaSchema(many=True)
        data = Drzava.query.filter(Drzava.id_kontinent==ID).all()
        if data:
            result = drzava_schema.dump(data)
            return jsonify(result)
        else:
            return make_response(jsonify({'error': 'Drzava with that id doesn\'t exist'})), 400

    elif flask.request.method == 'POST':
        err = flask.request.method + ' request not allowed'
        return make_response(jsonify({'error': err})), 405



@app.route('/api/drzave', methods=['GET', 'POST'])
@validate_token
def vrati_drzave():
    """
        vrati sve drzave, ili kreiraj novu
    """


    if flask.request.method == 'GET':
        drzava_schema = DrzavaSchema(many=True)
        data = Drzava.query.all()
        if data:
            result = drzava_schema.dump(data)
            return jsonify(result)
        else:
            return make_response(jsonify({'error': 'no Drzava found'})), 400

    elif flask.request.method == 'POST':
        drzava_schema = DrzavaSchema()
        payload = flask.request.get_json()
        for req in ['naziv','id_kontinent']:
            if req not in payload:
                return make_response(jsonify({'error':'Required parameters missing'})),400
            else:
                ima = Drzava.query.filter(Drzava.naziv == payload['naziv']).first()
                if not ima:
                    new_id = db.session.query(func.max(Drzava.id)).scalar()
                    new_id += 1
                    naziv = payload['naziv']
                    id_kontinent = payload['id_kontinent']
                    if 'opis' in payload:
                        opis  = payload['opis']
                    else:
                        opis = None
                    drzava = Drzava(id=new_id, naziv=naziv, opis=opis, id_kontinent=id_kontinent)
                    print(drzava)
                    db.session.add(drzava)
                    db.session.commit()
                    result = drzava_schema.dump(drzava)
                    return make_response(jsonify(result)), 200
                else:
                    return make_response(jsonify({'error': 'Drzava with that naziv already exists'})), 400

    else:
        err = flask.request.method + 'request not allowed'
        return make_response(jsonify({'error': err})), 405






@app.route('/api/drzave/<int:ID>', methods=['GET', 'PUT', 'DELETE'])
@validate_token
def vrati_drzavu(ID):
    """
        vrati drzavu po ID, izmeni je, ili obrisi
    """
    drzava_schema = DrzavaSchema()

    if flask.request.method == 'GET':
        data = Drzava.query.filter(Drzava.id==ID).first()
        if data:
            result = drzava_schema.dump(data)
            return jsonify(result)
        else:
            return make_response(jsonify({'error':'could not find Drzava with that ID'})), 404



    elif flask.request.method == 'PUT':
        data = Drzava.query.filter(Drzava.id==ID).first()
        if data:
            for arg in flask.request.get_json():
                if arg == 'naziv':
                    data.naziv = flask.request.get_json()[arg]
                elif arg == 'opis':
                    data.opis = flask.request.get_json()[arg]
                else:
                    pass
            db.session.commit()
            result = drzava_schema.dump(data)
            return make_response(jsonify(result)), 200
        else:
            return make_response(jsonify({'error':'could not find Drzava with that ID'})), 404



    elif flask.request.method == 'DELETE':
        ima = Drzava.query.filter(Drzava.id==ID).first()
        if ima:
            Drzava.query.filter(Drzava.id==ID).delete()
            db.session.commit()
            return make_response(jsonify({'status':'successfully deleted'})), 200
        else:
            return make_response(jsonify({'error':'could not find Drzava with that ID'})), 404

    else:
        err = flask.request.method + 'request not allowed'
        return make_response(jsonify({'error': err})), 405


@app.route('/api/drzave/<int:ID>/destinacije', methods=['GET', 'POST'])
@validate_token
def vrati_destinacije_drzave(ID):
    """
        vrati sve destinacije po ID drzave, ili dodaj novu
    """
    if flask.request.method == 'GET':

        data = Destinacija.query.filter(Destinacija.id_drzava==ID).all()
        destinacija_schema = DestinacijaSchema(many=True)
        result = destinacija_schema.dump(data)
        return make_response(jsonify(result),200)



    elif flask.request.method == 'POST':

        destinacija_schema = DestinacijaSchema()
        payload = flask.request.get_json()

        for req in ['naziv','cena_bus','cena_avion','cena_smestaj','last_min']:
            if req not in payload:
                return make_response(jsonify({'error':'Required parameter(s) missing'})),400

        new_id  = db.session.query(func.max(Destinacija.id)).scalar()
        print(type(new_id))
        if new_id == None:
            new_id=0
        new_id += 1
        naziv        = payload['naziv']
        cena_avion   = payload['cena_avion']
        cena_bus     = payload['cena_bus']
        cena_smestaj = payload['cena_smestaj']
        last_min     = payload['last_min']

        if 'opis' in payload:
            opis  = payload['opis']
        else:
            opis = None
        if 'zvezdice' in payload:
            zvezdice = payload['zvezdice']
        else:
            zvezdice = None

        dest = Destinacija(id=new_id, id_drzava=ID, naziv=naziv, opis=opis, zvezdice=zvezdice, cena_avion=cena_avion, cena_smestaj=cena_smestaj, cena_bus=cena_bus, last_min=last_min)

        db.session.add(dest)
        db.session.commit()

        result = destinacija_schema.dump(dest)
        return make_response(jsonify(result)), 200
    else:
        err = flask.request.method + 'request not allowed'
        return make_response(jsonify({'error': err})), 405


@app.route('/api/destinacije', methods=['GET', 'POST'])
@validate_token
def vrati_destinacije():
    """
        vrati sve destinacije, ili kreiraj novu
    """
    if flask.request.method == 'GET':
        destinacija_schema = DestinacijaSchema(many=True)
        data = Destinacija.query.all()
        result = destinacija_schema.dump(data)
        return jsonify(result)

    elif flask.request.method == 'POST':
        destinacija_schema = DestinacijaSchema()
        payload = flask.request.get_json()
        for req in ['naziv','id_drzava','cena_bus','cena_avion','cena_smestaj','last_min']:
            if req not in payload:
                return make_response(jsonify({'error':'Required parameters missing'})),400

        new_id = db.session.query(func.max(Destinacija.id)).scalar()
        print(type(new_id))
        if new_id == None:
            new_id=0
        new_id += 1
        naziv        = payload['naziv']
        cena_avion   = payload['cena_avion']
        cena_bus     = payload['cena_bus']
        cena_smestaj = payload['cena_smestaj']
        last_min     = payload['last_min']
        drzava_id    = payload['id_drzava']

        if 'opis' in payload:
            opis  = payload['opis']
        else:
            opis = None
        if 'zvezdice' in payload:
            zvezdice = payload['zvezdice']
        else:
            zvezdice = None

        dest = Destinacija(id=new_id, id_drzava=drzava_id, naziv=naziv, opis=opis, zvezdice=zvezdice, cena_avion=cena_avion, cena_smestaj=cena_smestaj, cena_bus=cena_bus, last_min=last_min, lajkovi=0, omiljeno=0)
        print(dest)
        db.session.add(dest)
        db.session.commit()
        result = destinacija_schema.dump(dest)
        return make_response(jsonify(result)), 200
    else:
        err = flask.request.method + 'request not allowed'
        return make_response(jsonify({'error': err})), 405


@app.route('/api/destinacije/<int:ID>', methods=['GET', 'PUT', 'DELETE'])
@validate_token
def vrati_destinaciju(ID):
    """
        vrati destinaciju po ID, izmeni je ili obrisi
    """
    destinacija_schema = DestinacijaSchema()
    if flask.request.method == 'GET':
        data = Destinacija.query.filter(Destinacija.id==ID).first()
        print(data)
        if data:
            result = destinacija_schema.dump(data)
            return jsonify(result)
        else:
            return make_response(jsonify({'error':'non-existing Destinacija'})),404


    elif flask.request.method == 'PUT':
        data = Destinacija.query.filter(Destinacija.id == ID).first()
        if data:
            for arg in flask.request.get_json():
                if arg == 'naziv':
                    data.naziv = flask.request.get_json()[arg]
                elif arg == 'hotel':
                    data.hotel = flask.request.get_json()[arg]
                elif arg == 'cena_bus':
                    data.cena_bus = flask.request.get_json()[arg]
                elif arg == 'cena_bus':
                    data.cena_bus = flask.request.get_json()[arg]
                elif arg == 'cena_avion':
                    data.cena_avion = flask.request.get_json()[arg]
                elif arg == 'cena_smestaj':
                    data.cena_smestaj = flask.request.get_json()[arg]
                elif arg == 'zvezdice':
                    data.zvezdice = flask.request.get_json()[arg]
                elif arg == 'lajkovi':
                    data.lajkovi = flask.request.get_json()[arg]
                elif arg == 'omiljeno':
                    data.omiljeno = flask.request.get_json()[arg]

                else:
                    pass
            db.session.commit()
            result = destinacija_schema.dump(data)
            return make_response(jsonify(result)), 200
        else:
            return make_response(jsonify({'error':'non-existing Destinacija'})),404


    elif flask.request.method == 'DELETE':
        ima = Destinacija.query.filter(Destinacija.id==ID).first()
        print('ojsa')
        if ima:
            aranzmani = Aranzman.query.filter(Aranzman.id == ima.id).all()
            print(len(aranzmani))
            Aranzman.query.filter(Aranzman.id_destinacija == ima.id).delete() 
            db.session.commit()
            Destinacija.query.filter(Destinacija.id==ID).delete()
            db.session.commit()
            return make_response(jsonify({'status':'successfully deleted'})), 200
        else:
            return make_response(jsonify({'error':'could not find Destinacija with that ID'})), 404

        #err = flask.request.method + 'request not allowed'
        #return make_response(jsonify({'error': err})), 405

@app.route('/api/admin/tokens', methods=['GET','PUT','POST', 'DELETE'])
def token_manager():
    """
        endpoint za upravljanje tokenima za autentifikaciju
        samo admini mogu da ga koriste, ako imaju secret_admin_token
        dozvoljava izmene, dodavanje i brisanje tokena
    """
    if flask.request.headers.get('MIT-API-TOKEN') == 'secret_admin_token':
        if flask.request.method == 'GET':
            token_schema = ApiTokenSchema(many=True)
            data = api_token.query.all()
            result = token_schema.dump(data)
            return make_response(jsonify(result)),200
        elif flask.request.method == 'PUT':
                data = api_token.query.filter(api_token.id == flask.request.args('id')).first()
                if data:
                    for arg in flask.request.args:
                        #if arg in data.__dict__:
                            #data.__dict__[arg] = flask.request.args[arg]
                            #print(data.__dict__)
                        if arg == 'token':
                            data.token = flask.request.args[arg]
                        elif arg == 'email':
                            data.email = flask.request.args[arg]
                        else:
                            pass
                        db.session.commit()
                    return make_response(jsonify({'status': 'success'})), 200
                else:
                    return make_response(jsonify({'error': 'token not found'})), 404

        elif flask.request.method == 'POST':
            api_token_schema = ApiTokenSchema()
            payload = flask.request.get_json()

            for req in ['token','email']:
                if req not in payload:
                    return make_response(jsonify({'error':'Required parameters missing'})),400
                else:
                    new_id  = db.session.query(func.max(api_token.id)).scalar()
                    new_id += 1
                    token   = payload['token']
                    email   = payload['email']


                    api_tok = api_token(id=new_id, token=token, email=email)
                    print(api_tok)
                    db.session.add(api_tok)
                    db.session.commit()
                    result = destinacija_schema.dump(api_tok)
                    return make_response(jsonify(result)), 200

        elif flask.request.method == 'DELETE':
            ID = flask.request.get_json()['token_id']
            if ID:
                ima = api_token.query.filter(api_token.id==ID).first()
            if ima:
                api_token.query.filter(api_token.id==ID).delete()
                db.session.commit()
                return make_response(jsonify({'status':'successfully deleted'})), 200
            else:
                return make_response(jsonify({'error':'could not find api token with that ID'})), 404
        else:
            err = flask.request.method + 'request not allowed'
            return make_response(jsonify({'error': err})), 405
    else:
        abort(404)




@app.route('/api/aranzmani', methods = ['GET','POST'])
@validate_token
def termini():
    if flask.request.method == 'GET':
        data = Aranzman.query.all()
        if data:
            aranzman_schema = AranzmanSchema(many=True)
            result = aranzman_schema.dump(data)
            return make_response(jsonify(result)),200
