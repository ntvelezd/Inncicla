from atexit import register
import re
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Estacion, Contacto, Usuario

admin.site.register(Estacion)
admin.site.register(Contacto)
admin.site.register(Usuario)
