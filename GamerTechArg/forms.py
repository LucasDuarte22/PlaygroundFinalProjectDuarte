from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class PlacasDeVideoFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    año = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    
class MotherboardsFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    año = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    
class AlmacenamientoFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    anio = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    
class MemoriasRAMFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    anio = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    
class ProcesadoresFormulario(forms.Form):
    marca = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=50)
    anio = forms.IntegerField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()
    
class UserRegisterForm(UserCreationForm):
 #    user = forms.TextInput(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
class UserEditForm(UserChangeForm):
    
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')


    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name']