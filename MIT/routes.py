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


@app.route('/kontinent/<string:kont>', methods=['GET'])
def kontinent(kont):
    kontinent = Kontinent.query.filter_by(naziv = kont)
    print(kont)
    print(kontinent)
    return render_template('kontinent.html', knt = kontinent)


@app.route('/drzava/<string:drz>', methods=['GET'])
def drzava(drz):
    return render_template('drzava.html')


@app.route('/destinacija', methods=['GET'])
def destinacija():
    return render_template('destinacija.html')


@app.route('/onama')
def onama():
    return render_template('onama.html')


@app.errorhandler(404)
def vrati_404(error):
    return render_template('404.html'), 404
