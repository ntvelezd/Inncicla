
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=30, required=True, help_text='Tu Nombre completo.')
    last_name = forms.CharField(label='Apellidos', max_length=30, required=True, help_text='Tus dos apellidos.')
    email = forms.EmailField(label='Correo', max_length=254, help_text='Tu correo electrónico', required=True)
    birth_date = forms.DateField(label='Fecha de nacimiento', help_text='Requerido en formato: YYYY-MM-DD', required=True)
    blood_types=(
        ("1", "O-"),
        ("2", "O+"),
        ("3", "A+"),
        ("4", "A-"),
        ("5", "B+"),
        ("6", "B-"),
        ("7", "AB+"),
        ("8", "AB-"),
    )
    blood_type = forms.ChoiceField(label='Tipo de sangre', choices=blood_types, required=True)
    phone = forms.CharField(label='Teléfono', max_length=30, required=True)
    Id_types=(
        ("1", "Tarjeta de Identidad"),
        ("2","Cédula de Ciudadanía"),
    )
    Id_type = forms.ChoiceField(label='Tipo de documento', choices=Id_types, required=True)
    Id_number = forms.CharField(label='Número de documento',  max_length=30, required=True)
    private_info = forms.ChoiceField(label='¿Aceptas compartir información personal?', choices=(("1","No"), ("2","Si")), required=True)
    disability = forms.ChoiceField(label='¿Tienes Alguna discapacidad?', choices=(("1","No"), ("2","Si")), required=True)
    about = forms.CharField(label='Cuéntanos de que se trata', max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2', )

class AgregarContactoForm(forms.Form):
 
    nombre = forms.CharField(label='Nombre', max_length=30, required=True, help_text='Tu Nombre completo.')
    apellido = forms.CharField(label='Apellido', max_length=30, required=True, help_text='Tu Apellido completo.')
    parentesco=(
        ("1", "Mamá"),
        ("2", "Papá"),
        ("3", "Hermano/a"),
        ("4", "Familiar"),
        ("5", "Amigo"),
        ("6", "Conocido"),
    )
    parentesco = forms.ChoiceField(label='Parentesco', choices=parentesco, required=True)
    telefono = forms.CharField(
                     help_text = "Celular"
                     )
    correo = forms.EmailField(label='Correo', max_length=254, help_text='Tu correo electrónico', required=True)
    Id_types=(
        ("1", "Tarjeta de Identidad"),
        ("2","Cédula de Ciudadanía"),
    )
    Id_type = forms.ChoiceField(label='Tipo de documento', choices=Id_types, required=True)
    Id_number = forms.CharField(label='Número de documento',  max_length=30, required=True)

    