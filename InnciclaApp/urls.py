from django.urls import include, path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home/', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
]