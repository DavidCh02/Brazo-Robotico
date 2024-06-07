from django.db import models
from datetime import datetime
class ControlRemoto(models.Model):
    estado_conexionWifi = models.BooleanField(default=False)
    estado_conexionBluetooth = models.BooleanField(default=False)

    def conectar(self):
        self.estado_conexionWifi = True
        self.estado_conexionBluetooth = True
        self.save()

    def desconectar(self):
        self.estado_conexionWifi = False
        self.estado_conexionBluetooth = False
        self.save()

    def controlarBrazo(self):
        print("Controlando el brazo")

    def __str__(self):
        return f"Control Remoto - Conectado: {self.estado_conexionWifi and self.estado_conexionBluetooth}"


class ESP32CAM(models.Model):
    resolucion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    Bluetooth = True
    Wifi = True

    def iniciarTransmision(self):
        self.estado = True
        self.save()

    def deternerTransmision(self):
        self.estado = False
        self.save()

    def __str__(self):
        return f"ESP32-CAM - Resolución: {self.resolucion} - Estado: {self.estado}"


class RegistroResiduos(models.Model):
    analisisResiduos = ()

    def registrar_residuo(self, residue):
        self.analisisResiduos.add(residue)
        self.save()

    def obtener_residuos(self):
        return self.analisisResiduos.all()

    def __str__(self):
        return "Sistema de Recolección"
class ServoPinza:
    def __init__(self):
        pass

    def mover(self):
        # Lógica para mover el servo de la pinza
        pass

class ServoBase:
    def __init__(self):
        pass

    def mover(self):
        # Lógica para mover el servo de la base
        pass

class ServoBrazo:
    def __init__(self):
        pass

    def mover(self):
        # Lógica para mover el servo del brazo
        pass

class ServoAntebrazo:
    def __init__(self):
        pass

    def mover(self):
        # Lógica para mover el servo del antebrazo
        pass

class BrazoRobotico:
    def __init__(self):
        self.__estado = "inactivo"
        self.__posicionActual = 0.0
        self.servo_pinza = ServoPinza()
        self.servo_base = ServoBase()
        self.servo_brazo = ServoBrazo()
        self.servo_antebrazo = ServoAntebrazo()

    def moverBase(self, posicion):
        self.servo_base.mover()
        # Lógica para mover la base

    def moverBrazo(self, posicion):
        self.servo_brazo.mover()
        # Lógica para mover el brazo

    def moverAnteBrazo(self, posicion):
        self.servo_antebrazo.mover()
        # Lógica para mover el antebrazo

    def pinza(self, estado):
        self.servo_pinza.mover()
        # Lógica para controlar la pinza

class SensorPeso:
    def __init__(self):
        self.peso = 0.0

    def calcularPeso(self, nuevo_peso):
        self.peso = nuevo_peso
        return self.peso

    def __str__(self):
        return f"Sensor Peso - {self.peso} kg"
