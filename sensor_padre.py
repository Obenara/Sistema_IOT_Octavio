from sensor_abuelo import SensorAbuelo

class SensorPadre(SensorAbuelo):
    def __init__(self, id, ubicacion, valor_inicial):
        super().__init__(id, ubicacion)
        self.valor = valor_inicial
