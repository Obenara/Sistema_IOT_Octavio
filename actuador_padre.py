from actuador_abuelo import ActuadorAbuelo

class ActuadorPadre(ActuadorAbuelo):
    def __init__(self, id, ubicacion, tipo):
        super().__init__(id, ubicacion)
        self.tipo = tipo

    def estado_actual(self):
        return f"[{self.id}] {self.tipo} en {self.ubicacion}: {'Encendido' if self.estado else 'Apagado'}"
