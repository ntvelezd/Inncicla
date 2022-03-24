from msilib.schema import CheckBox
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', max_length=30, required=False, help_text='Tu Nombre completo.')
    last_name = forms.CharField(label='Apellidos', max_length=30, required=False, help_text='Tus dos apellidos.')
    email = forms.EmailField(label='Correo', max_length=254, help_text='Tu correo electrónico', required=False)
    birth_date = forms.DateField(label='Fecha de nacimiento', help_text='Requerido en formato: YYYY-MM-DD', required=False)
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
    blood_type = forms.ChoiceField(label='Tipo de sangre', choices=blood_types, required=False)
    phone = forms.CharField(label='Teléfono', max_length=30, required=False)
    Id_types=(
        ("1", "Tarjeta de Identidad"),
        ("2","Cédula de Ciudadanía"),
    )
    Id_type = forms.ChoiceField(label='Tipo de documento', choices=Id_types, required=False)
    Id_number = forms.CharField(label='Número de documento',  max_length=30, required=False)
    private_info = forms.ChoiceField(label='¿Aceptas compartir información personal?', choices=(("1","No"), ("2","Si")), required=False)
    disability = forms.ChoiceField(label='¿Tienes Alguna discapacidad?', choices=(("1","No"), ("2","Si")), required=False)
    about = forms.CharField(label='Cuéntanos de que se trata', max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2', )