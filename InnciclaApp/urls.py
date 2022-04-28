from django.urls import include, path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('home/', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    path('estaciones/', views.estaciones, name="estaciones"),
]
