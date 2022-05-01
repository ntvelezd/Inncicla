from atexit import register
import re
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Estacion

admin.site.register(Estacion)
