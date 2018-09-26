from mit import db
import datetime



class Kontinent(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)



class Drzava(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)
    slika_URL       = db.Column(db.String(250), index=True)
    opis            = db.Column(db.String(250), index=True, unique=True)

    id_kontinent    = db.Column(db.Integer, db.ForeignKey('kontinent.id'), primary_key=True)
    kontinent       = db.relationship('Kontinent', backref='drzava', lazy=True)




class Aranzman(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    id_destinacija  = db.Column(db.Integer, db.ForeignKey('destinacija.id', ondelete='CASCADE'), primary_key=True)
    destinacija     = db.relationship('Destinacija', backref='destinacija', lazy=True)
    dat_pol         = db.Column(db.String(64))
    dat_dol         = db.Column(db.String(64))

    aranzman = db.relationship('Destinacija', backref=db.backref('aranzman', passive_deletes=True))



class Destinacija(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True)
    hotel           = db.Column(db.String(64))
    opis            = db.Column(db.String(600), index=True)
    zvezdice        = db.Column(db.Integer, index=True)
    cena_smestaj    = db.Column(db.Integer, unique=False)
    cena_avion      = db.Column(db.Integer, unique=False)
    cena_bus        = db.Column(db.Integer, unique=False)
    last_min        = db.Column(db.Boolean, unique=False)
    id_drzava       = db.Column(db.Integer)
    slika_URL       = db.Column(db.String(255))
    lajkovi         = db.Column(db.Integer)
    omiljeno        = db.Column(db.Integer)
    url             = db.Column(db.String(255))

    aranzmani = db.relationship('Aranzman', passive_deletes=True)

class api_token(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    token           = db.Column(db.String(250), index=True, unique=True)
    email           = db.Column(db.String(250), index=True, unique=True)
