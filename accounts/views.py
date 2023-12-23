from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileUserForm


#SIGNUP-LOGIN
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form = EditProfileUserForm
    template_name = "editar_perfil.html"
    success_url = reverse_lazy('Inicio')
    
class UserLoginView(LoginView):
    template_name = "login.html"

