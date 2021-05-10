""" models posts """
# Create your models here.
# my database will be here

# users models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class NewProblem(models.Model):
    """Class to generate new problem
    Args:
        latitud ([float]) blank=False
        longitud ([float]) blank=False
        tipo_problema ([str]) blank=False
        nivel_prioridad ([str]) blank=False
        ciudad ([str]) null=True
        estado ([str]) blank=False
        codigo_postal ([str]) null=True
        informacion_extra ([str]) null=True
    Returns:
        array-string with longitud, latitud, tipo_problema, nivel_prioridad, estado
    """
    
    latitud = models.FloatField(blank=False) # no puede quedar vacio
    longitud = models.FloatField(blank=False) # no puede quedar vacio
    tipo_problema = models.CharField(max_length = 35, blank=False) # no puede quedar vacio
    nivel_prioridad = models.CharField(max_length = 19, blank=False) # no puede quedar vacio
    ciudad = models.CharField( max_length=50, null=True)
    estado = models.CharField(max_length = 3, blank=False) # no puede quedar vacio
    codigo_postal = models.CharField(max_length = 5, null=True)
    informacion_extra = models.TextField(max_length = 256, null=True)
    
    def __str__(self):
        return f"Longitud: {self.longitud} Latitud: {self.latitud}\
        \nTipo de problema: {self.tipo_problema}\nNivel de prioridad: {self.nivel_prioridad}\
        \nEstado: {self.estado}"