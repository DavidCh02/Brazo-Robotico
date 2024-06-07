from django.contrib import admin
from .models import User, Residue, RoboticArmAction, ControlRemoto, BrazoRobotico, ESP32CAM, SensorPeso, Bluetooth, SistemaRecoleccion

admin.site.register(User)
admin.site.register(Residue)
admin.site.register(RoboticArmAction)
admin.site.register(ControlRemoto)
admin.site.register(BrazoRobotico)
admin.site.register(ESP32CAM)
admin.site.register(SensorPeso)
admin.site.register(Bluetooth)
admin.site.register(SistemaRecoleccion)
