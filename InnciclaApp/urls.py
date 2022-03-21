from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name="signup"),
]