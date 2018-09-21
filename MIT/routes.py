from mit import app
from mit import db
from flask import render_template

from models import *

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
	drzava = Drzava.query.filter(Drzava.naziv==drz.title()).first()
	if drzava:
		destinacije = Destinacija.query.filter(Destinacija.id_drzava == drzava.id).all()
        return render_template('drzava.html', drzava=drzava, dest = destinacije)


@app.route('/destinacija/<string:dest>', methods=['GET'])
def destinacija(dest):
    dest = Destinacija.query.filter(Destinacija.naziv==dest).first()
    print(dest)
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


@app.route('/search/<string:keyword>', methods=['GET'])
def pretraga(keyword):
    drzava = Drzava.query.filter(Drzava.naziv.like(keyword)).first()
    if drzava:
        destinacije = Destinacija.query.filter(Destinacija.id_drzava == drzava.id ).all()       
    return render_template('pretraga.html', drzave = drzava, destinacije = destinacije)




@app.errorhandler(404)
def vrati_404(error):
    return render_template('404.html'), 404
