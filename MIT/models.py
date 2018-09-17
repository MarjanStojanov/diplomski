from mit import db
import datetime
class Kontinent(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)
    slika_URL       = db.Column(db.String(250), index=True, unique=True)

    def __str__(self):
        return self.naziv

class Drzava(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)
    slika_URL       = db.Column(db.String(250), index=True, unique=True)
    opis            = db.Column(db.String(250), index=True, unique=True)


    def toJSON(self):
        return {
        'id':self.id,
        'naziv':self.naziv,
        'opis':self.opis
        }


class Aranzman(db.Model):
    __table_args__  = {'extend_existing': True}
    id_termin       = db.Column(db.Integer, db.ForeignKey('destinacija.id'), primary_key=True)
    id_dest         = db.Column(db.Integer, db.ForeignKey('termin.id'), primary_key=True)

    destinacija     = db.relationship('Destinacija', backref='Aranzman', lazy=True)
    termin          = db.relationship('Termin', backref='Aranzman', lazy=True)


class Destinacija(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    naziv           = db.Column(db.String(64), index=True, unique=True)
    opis            = db.Column(db.String(600), index=True, unique=True)
    zvezdice        = db.Column(db.Integer, index=True, unique=False)
    cena_smestaj    = db.Column(db.Integer, unique=False)
    cena_avion      = db.Column(db.Integer, unique=False)
    cena_bus        = db.Column(db.Integer, unique=False)
    last_min        = db.Column(db.Boolean, unique=False)

    drzava          = db.relationship('Drzava', backref='drzava', lazy=True)
    id_drzava       = db.Column(db.Integer, db.ForeignKey('drzava.id'))



class Termin(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    dat_pol         = db.Column(db.DateTime)
    dat_dol         = db.Column(db.DateTime)


class api_token(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    token           = db.Column(db.String(250), index=True, unique=True)
    email           = db.Column(db.String(250), index=True, unique=True)
