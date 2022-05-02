from django.urls import include, path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    path('estaciones/', views.estaciones, name="estaciones"),
    path('contactos/', views.contactos, name="contactos"),
    path('contacto-info/', views.contactoInfo, name="contacto-info"),
    path('contacto-agregar/', views.contactoAgregar, name="contacto-agregar"),
    path('mapa/', views.mapa, name="mapa"),
    path('busqueda/', views.busqueda, name="busqueda"),
]
