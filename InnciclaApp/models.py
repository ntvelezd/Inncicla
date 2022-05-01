from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Estacion(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30)
    maps = models.URLField(max_length = 200)
    image = models.CharField(max_length = 200, default = "css/images/floresta.jpg")