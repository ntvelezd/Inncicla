from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Estacion(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30)
    maps = models.URLField(max_length = 200)
    image = models.CharField(max_length = 200, default = "css/images/floresta.jpg")

class Contacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=30)
    numeroDoc = models.CharField(max_length=30)

class Usuario(models.Model):
    nombre = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    birth_date = models.CharField(max_length = 100)
    blood_type = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    Id_type = models.CharField(max_length = 100)
    Id_number = models.CharField(max_length = 30)
    private_info = models.CharField(max_length = 30)
    disability = models.CharField(max_length = 30)
    about = models.CharField(max_length = 500)
    id_contacto = models.CharField(max_length = 30)