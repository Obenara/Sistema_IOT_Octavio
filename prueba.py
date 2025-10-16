from sensores_hijos import SensorTemperatura, SensorHumedad, SensorCO2
from actuadores_hijos import Ventilador, Luz, Humidificador
from sensor_abuelo import SensorAbuelo


def ejecutar_sistema():
    # Sensores
    sensores = [
        SensorTemperatura("T1", "Sala", 25),
        SensorHumedad("H1", "Sala", 30),
        SensorCO2("C1", "Laboratorio", 1200)
    ]

    # Actuadores
    ventilador = Ventilador("V1", "Laboratorio")
    luz = Luz("L1", "Sala")
    humidificador = Humidificador("HU1", "Sala")

    actuadores = [ventilador, luz, humidificador]

    print("=== LECTURA DE SENSORES ===")
    for s in sensores:
        print(s.leer())
        print(s.calibrar())

    # Activación basada en condiciones
    acciones = []
    for s in sensores:
        if isinstance(s, SensorCO2) and s.valor > 1000:
            acciones.append(ventilador.activar())
        if isinstance(s, SensorHumedad) and s.valor < 40:
            acciones.append(humidificador.activar())
        if isinstance(s, SensorTemperatura) and s.valor < 20:
            acciones.append(luz.activar())

    print("\n=== REPORTE DE ACCIONES ===")
    for a in acciones:
        print(a)

    print(f"\nTotal de sensores: {SensorAbuelo.contar_sensores()}")
    print(f"Ventilador: {'Encendido' if ventilador.estado else 'Apagado'}")
    print(f"Luz: {'Encendida' if luz.estado else 'Apagada'}")
    print(f"Humidificador: {'Encendido' if humidificador.estado else 'Apagado'}")

if __name__ == "__main__":
    ejecutar_sistema()
