from django.db import models
from django.http import HttpResponse
import requests
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

    def _str_(self):
        return f"Control Remoto - Conectado: {self.estado_conexionWifi and self.estado_conexionBluetooth}"

class ESP32CAM(models.Model):
    resolucion = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)

    def iniciarTransmision(self):
        self.estado = True
        self.save()

    def detenerTransmision(self):
        self.estado = False
        self.save()

    def _str_(self):
        return f"ESP32-CAM - Resolución: {self.resolucion} - Estado: {self.estado}"