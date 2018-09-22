from mit import app
from mit import db
from flask import render_template, make_response, abort
import hashlib
from models import *
import flask
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/kontinenti', methods=['GET'])
def kontinenti():
    return render_template('kontinenti.html')


@app.route('/kontinent/<string:kont>/drzave', methods=['GET'])
def kontinent(kont):
	print(kont)
	kontinent = Kontinent.query.filter(Kontinent.naziv == kont).first()
	if kontinent:
		drzave = Drzava.query.filter(Drzava.id_kontinent == kontinent.id).all()
		return render_template('kontinent.html', knt = kontinent, drzave = drzave)


@app.route('/drzava/<string:drz>', methods=['GET'])
def drzava(drz):
    print(drz)
    drzava = Drzava.query.filter(Drzava.naziv==drz.title()).first()
    if drzava:
        destinacije = Destinacija.query.filter(Destinacija.id_drzava == drzava.id).all()
        return render_template('drzava.html', drzava=drzava, dest = destinacije)
    return render_template('404.html')


@app.route('/destinacija/<string:destin>', methods=['GET'])
def destinacija(destin):
    dest = Destinacija.query.filter(Destinacija.naziv==destin).first()
    if dest:
        aranzmani = Aranzman.query.filter(Aranzman.id_destinacija==dest.id).all()
        print(aranzmani)
        return render_template('destinacija.html', dest=dest, aranzmani = aranzmani)
    return render_template('404.html')

@app.route('/onama', methods=['GET'])
def onama():
	return render_template('onama.html')

@app.route('/kontakt', methods=['GET'])
def kontakt():
	return render_template('kontakt.html')

@app.route('/token', methods=['GET','POST'])
def token():
    if flask.request.method == 'GET':
        print('oyyyyyy')
        return render_template('token.html')
    elif flask.request.method == 'POST':
        from sqlalchemy.sql.expression import func
        exists = api_token.query.filter(api_token.email == flask.request.form['email']).first()
        if exists:
            return "USER ALREADY EXISTS"
        else:
            new_id = db.session.query(func.max(api_token.id)).scalar()
            print(new_id)
            if new_id is not None:
                new_id += 1
            else:
                new_id  = 0
            string = app.config['SECRET_KEY'] + flask.request.form['email']
            token = hashlib.md5(string)

            api_tok = api_token(id = new_id, token = token.hexdigest(), email=flask.request.form['email'])
            db.session.add(api_tok)
            db.session.commit()

            return str(token.hexdigest())
    else:
         abort(403)



@app.route('/search/<string:keyword>', methods=['GET'])
def pretraga(keyword):
    drzava = Drzava.query.filter(Drzava.naziv.like(keyword)).first()
    if drzava:
        destinacije = Destinacija.query.filter(Destinacija.id_drzava == drzava.id ).all()
        return render_template('pretraga.html', drzave = drzava, destinacije = destinacije)
    else:
        destinacije2 = Destinacija.query.filter(Destinacija.naziv.like(keyword)).all()
        if destinacije2:
            return render_template('pretraga.html', destinacije = destinacije2)




@app.errorhandler(404)
def vrati_404(error):
    return render_template('404.html'), 404
