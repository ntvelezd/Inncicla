from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.utils import timezone
from InnciclaApp.models import Estacion, Contacto
from InnciclaApp.forms import SignUpForm
from .forms import AgregarContactoForm

# Create your views here.
def inicio(request):
    return render(request, 'InnciclaApp/inicio.html', {})

def home(request):
    return render(request,"InnciclaApp/home.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def estaciones(request):
    estaciones = Estacion.objects.all()
    context = {
        "estaciones" : estaciones,
    }
    
    return render(request,"InnciclaApp/estaciones.html", context)

def busqueda(request):
   q = request.GET.get('q', '')
   estaciones = Estacion.objects.filter(nombre__icontains = q)
   context = {
       "estaciones" : estaciones,
   }
   return render(request, 'InnciclaApp/estaciones.html', context)

def contactos(request):
    contactos = Contacto.objects.all()
    context = {
        "contactos" : contactos,
    }

    return render(request,"InnciclaApp/Contactos/contactos.html", context)

def contactoInfo(request):
    
    return render(request,"InnciclaApp/Contactos/contacto-info.html")

def contactoAgregar(request):
    if request.method == "POST":
        form = AgregarContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.author = request.user
            contacto.published_date = timezone.now()
            contacto.save()
            return redirect('contactos', pk=contacto.pk)
    else:
        form = AgregarContactoForm()

    context ={}
    context['form']= form
    return render(request, "InnciclaApp/Contactos/contacto-agregar.html", context)
    
def mapa(request):
    return render(request,"InnciclaApp/mapa.html")

def crearUsuario(request):
    return render(request,"InnciclaApp/Admin/crear_usuario.html")

