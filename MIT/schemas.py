from mit import ma

class KontinentSchema(ma.Schema):
	class Meta:
		fields = ('id','naziv')
class DrzavaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('naziv', 'id', 'opis','id_kontinent')

class DestinacijaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'naziv', 'opis', 'zvezdice', 'cena_smestaj', 'cena_bus', 'cena_avion', 'last_min', 'id_drzava')


class ApiTokenSchema(ma.Schema):
    class Meta:
        fields = ('id', 'token', 'email')

class TerminSchema(ma.Schema):
	class Meta:
		fields = ('id', 'id_termin', 'dat_pol', 'dat_dol')