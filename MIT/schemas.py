from mit import ma
class DrzavaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('naziv', 'id', 'opis')

class DestinacijaSchema(ma.Schema):
    class Meta:
        fiels = ('id', 'naziv', 'opis', 'zvezdice', 'cena_smestaj', 'cena_bus', 'cena_avion', 'last_min', 'drzava_id')


class ApiTokenSchema(ma.Schema):
    class Meta:
        fiels = ('id', 'token', 'email')
