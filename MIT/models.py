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

    drzava          = db.relationship('Destinacija', backref='drzava', lazy=True)
    id_drzava       = db.Column(db.Integer, db.ForeignKey('destinacija.id'))




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

    #aranzman        = db.relationship('Aranzman', backref='Destinacija', lazy=True)



class Termin(db.Model):
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer, primary_key=True)
    dat_pol         = db.Column(db.DateTime)
    dat_dol         = db.Column(db.DateTime)

    #aranzman        = db.relationship('Aranzman', backref='Termini', lazy=True)


class api_token(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    token            = db.Column(db.String(250), index=True, unique=True)
    email           = db.Column(db.String(250), index=True, unique=True)
