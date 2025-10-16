from abc import ABC, abstractmethod

class ActuadorAbuelo(ABC):
    def __init__(self, id, ubicacion):
        self.id = id
        self.ubicacion = ubicacion
        self.estado = False

    @abstractmethod
    def activar(self):
        pass

    def desactivar(self):
        self.estado = False
        return f"[{self.id}] Actuador desactivado en {self.ubicacion}"
