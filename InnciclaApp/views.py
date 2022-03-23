from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


# Create your views here.
def post_list(request):
    return render(request, 'InnciclaApp/primerTemplate.html', {})

def home(request):
    return render(request,"InnciclaApp/home.html")

def estaciones(request):
    return render(request,"InnciclaApp/estaciones.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"