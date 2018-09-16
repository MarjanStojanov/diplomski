from mit import ma
class DrzavaSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('naziv', 'id', 'opis')

class DestinacijaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'naziv', 'opis', 'zvezdice', 'cena_smestaj', 'cena_bus', 'cena_avion', 'last_min', 'id_drzava')


class ApiTokenSchema(ma.Schema):
    class Meta:
        fiels = ('id', 'token', 'email')
