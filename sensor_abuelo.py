from abc import ABC, abstractmethod

class SensorAbuelo(ABC):
    total_sensores = 0

    def __init__(self, id, ubicacion):
        self.id = id
        self.ubicacion = ubicacion
        SensorAbuelo.total_sensores += 1

    @abstractmethod
    def leer(self):
        pass

    def calibrar(self):
        return f"[{self.id}] Sensor en {self.ubicacion} calibrado"

    @classmethod
    def contar_sensores(cls):
        return cls.total_sensores
