from mit import ma

class KontinentSchema(ma.Schema):
	class Meta:
		fields = ('id','naziv')
class DrzavaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('naziv', 'id', 'opis','id_kontinent', 'slika_URL')

class DestinacijaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'naziv', 'hotel', 'opis', 'zvezdice', 'cena_smestaj', 'cena_bus', 'cena_avion', 'last_min','lajkovi', 'omiljeno', 'id_drzava')


class ApiTokenSchema(ma.Schema):
    class Meta:
        fields = ('id', 'token', 'email')

class AranzmanSchema(ma.Schema):
	class Meta:
		fields = ('id', 'id_destinacija', 'dat_pol', 'dat_dol')
