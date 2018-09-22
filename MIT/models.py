from mit import db
import datetime



class Kontinent(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)
    #slika_URL       = db.Column(db.String(250), index=True, unique=True)




class Drzava(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)
    slika_URL       = db.Column(db.String(250), index=True, unique=True)
    opis            = db.Column(db.String(250), index=True, unique=True)

    id_kontinent    = db.Column(db.Integer, db.ForeignKey('kontinent.id'), primary_key=True)
    kontinent       = db.relationship('Kontinent', backref='drzava', lazy=True)




class Aranzman(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    id_destinacija  = db.Column(db.Integer, db.ForeignKey('destinacija.id'), primary_key=True)
    destinacija     = db.relationship('Destinacija', backref='aranzman', lazy=True)
    dat_pol         = db.Column(db.String(64))
    dat_dol         = db.Column(db.String(64))


class Destinacija(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)
    hotel           = db.Column(db.String(64))
    opis            = db.Column(db.String(600), index=True, unique=True)
    zvezdice        = db.Column(db.Integer, index=True, unique=False)
    cena_smestaj    = db.Column(db.Integer, unique=False)
    cena_avion      = db.Column(db.Integer, unique=False)
    cena_bus        = db.Column(db.Integer, unique=False)
    last_min        = db.Column(db.Boolean, unique=False)
    id_drzava       = db.Column(db.Integer)

    lajkovi         = db.Column(db.Integer)
    omiljeno        = db.Column(db.Integer)
    url             = db.Column(db.String(255))

"""
    will probably kick this out, Aranzman has everything needed

class Termin(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)

"""
class api_token(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    token           = db.Column(db.String(250), index=True, unique=True)
    email           = db.Column(db.String(250), index=True, unique=True)
