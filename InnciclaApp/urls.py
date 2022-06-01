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
    path('crear-usuario/', views.crearUsuario, name="crear-usuario"),
    path('ver-usuario/', views.verUsuario, name="ver-usuario"),
    path('menu-admin/', views.menuAdmin, name="menu-admin"),
    path('mapa/', views.mapa, name="mapa"),
    path('busqueda/', views.busqueda, name="busqueda"),
]
