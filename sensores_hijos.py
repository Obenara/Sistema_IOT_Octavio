from sensor_padre import SensorPadre

class SensorTemperatura(SensorPadre):
    def __init__(self, id, ubicacion, celsius):
        super().__init__(id, ubicacion, celsius)

    def leer(self):
        return f"[{self.id}] Temperatura en {self.ubicacion}: {self.valor}°C"

    @staticmethod
    def c_a_f(c):
        return round((c * 9 / 5) + 32, 2)


class SensorHumedad(SensorPadre):
    def __init__(self, id, ubicacion, porcentaje):
        super().__init__(id, ubicacion, porcentaje)

    def leer(self):
        return f"[{self.id}] Humedad en {self.ubicacion}: {self.valor}%"


class SensorCO2(SensorPadre):
    def __init__(self, id, ubicacion, ppm):
        super().__init__(id, ubicacion, ppm)

    def leer(self):
        return f"[{self.id}] CO2 en {self.ubicacion}: {self.valor} ppm"
