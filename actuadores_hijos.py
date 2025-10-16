from actuador_padre import ActuadorPadre

class Ventilador(ActuadorPadre):
    def __init__(self, id, ubicacion):
        super().__init__(id, ubicacion, "Ventilador")

    def activar(self):
        self.estado = True
        return f"[{self.id}] Ventilador encendido en {self.ubicacion}"


class Luz(ActuadorPadre):
    def __init__(self, id, ubicacion):
        super().__init__(id, ubicacion, "Luz")

    def activar(self):
        self.estado = True
        return f"[{self.id}] Luz encendida en {self.ubicacion}"


class Humidificador(ActuadorPadre):
    def __init__(self, id, ubicacion):
        super().__init__(id, ubicacion, "Humidificador")

    def activar(self):
        self.estado = True
        return f"[{self.id}] Humidificador encendido en {self.ubicacion}"
