﻿from mit import app
from mit import db
from flask import render_template, make_response, abort, jsonify
import hashlib
from models import *
import flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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
    drzava = Drzava.query.filter(Drzava.naziv==drz).first()
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
            token = hashlib.sha256(string.encode('utf-8'))

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
        else:
            return render_template('pretraga.html', destinacije = None, drzave = None)


@app.route('/sendemail', methods=['POST'])
def salji_mejl():
    """
        Ova funkcija povlači podatke iz AJAX zahteva, formatira email
        i salje ga na određenu adresu
    """
    print(flask.request.data)
    print(flask.request.get_json())

    fromaddr = app.config['MAIL_USERNAME']
    toaddr = flask.request.get_json()['email']
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = flask.request.get_json()['subject']
    body = flask.request.get_json()['name']  + ' ' + flask.request.get_json()['surname'] + ' je postavio pitanje:\n\n\n' + flask.request.get_json()['message'] #flask.request.form['message']
    msg.attach(MIMEText(body, 'plain'))

    print('sending mail to ' + toaddr + ' on ' + msg['Subject'])

    mailServer = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    mailServer.login(fromaddr, app.config['MAIL_PW'])
    mailServer.sendmail(fromaddr, toaddr, msg.as_string())
    mailServer.quit()
    return "success"


@app.errorhandler(404)
def vrati_404(error):
    if 'MIT-API-TOKEN' in flask.request.headers:
        return jsonify({'error':'endpoint not found'}),404
    else:
        return render_template('404.html'), 404
