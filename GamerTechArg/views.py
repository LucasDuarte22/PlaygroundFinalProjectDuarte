
from django.http import HttpResponse
from django.shortcuts import render,redirect
from GamerTechArg.forms import PlacasDeVideoFormulario, MotherboardsFormulario, ProcesadoresFormulario, AlmacenamientoFormulario, MemoriasRAMFormulario,UserRegisterForm, UserEditForm
from .models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
#LOGIN
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def inicio(request):
    return render(request, 'GamerTechArg/inicio.html')

def user_logout(request):
    logout(request)
    return redirect("GamerTechArg:index.html")

def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, instance=request.user)
        
        if miFormulario.is_valid():
            miFormulario.save()
            return render(request, "GamerTechArg/inicio.html")
        
    else:
        miFormulario = UserEditForm(instance=request.user)
    return render(request, "GamerTechArg/editarPerfil.html", {"miFormulario":miFormulario, "usuario": usuario})


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    template_name = "GamerTechArg/cambiar_contraseña.html"
    success_url = reverse_lazy('EditarPerfil')
    

#COMPONENTES:
def placasdevideo(request):
    if request.method == "POST":
        
        miFormulario = PlacasDeVideoFormulario(request.POST) # Aqui me llega la informacion del html
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            placas_de_video = PlacasDeVideo(marca=informacion["marca"],modelo=informacion["modelo"], año=informacion["año"], descripcion=informacion["descripcion"], precio=informacion["precio"])
            placas_de_video.save()
            return render(request, "GamerTechArg/inicio.html")
    else:
        miFormulario = PlacasDeVideoFormulario()
    return render(request, "GamerTechArg/placas.html", {"miFormulario": miFormulario})



def motherboards(request):
    if request.method == "POST":
        miFormulario = MotherboardsFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            mother_board = Motherboards(marca=informacion["Marca"],modelo=informacion["Modelo"], anio=informacion["Año"], descripcion=informacion["Descripcion"], precio=informacion["Precio"])
            mother_board.save()
            return render(request, "GamerTechArg/inicio.html")
    else:
        miFormulario = MotherboardsFormulario()
    return render(request, "GamerTechArg/motherboards.html", {"miFormulario": miFormulario})


def almacenamiento(request):
    if request.method == "POST":
        miFormulario = AlmacenamientoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            storage = Almacenamiento(marca=informacion["Marca"],modelo=informacion["Modelo"], anio=informacion["Año"], descripcion=informacion["Descripcion"], precio=informacion["Precio"])
            storage.save()
            return render(request, "GamerTechArg/inicio.html")
    else:
        miFormulario = AlmacenamientoFormulario()
    return render(request, "GamerTechArg/almacenamiento.html", {"miFormulario": miFormulario})


def memoriasram(request):
    if request.method == "POST":
        miFormulario = MemoriasRAMFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            ram = MemoriasRAM(marca=informacion["Marca"],modelo=informacion["Modelo"], anio=informacion["Año"], descripcion=informacion["Descripcion"], precio=informacion["Precio"])
            ram.save()
            return render(request, "GamerTechArg/inicio.html")
    else:
        miFormulario = MemoriasRAMFormulario()
    return render(request, "GamerTechArg/memoriasram.html", {"miFormulario": miFormulario})


def procesadores(request):
    if request.method == "POST":
        miFormulario = ProcesadoresFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            processors = Procesadores(marca=informacion["Marca"],modelo=informacion["Modelo"], anio=informacion["Año"], descripcion=informacion["Descripcion"], precio=informacion["Precio"])
            processors.save()
            return render(request, "GamerTechArg/inicio.html")
    else:
        miFormulario = ProcesadoresFormulario()
    return render(request, "GamerTechArg/procesadores.html", {"miFormulario": miFormulario})


def leer_placas(request):
    
    placas = PlacasDeVideo.objects.all()
    contexto = {"placas": placas}
    
    return render(request, "GamerTechArg/leerPlacas.html",contexto)


def leer_motherboards(request):
    
    mother_boards = Motherboards.all()
    contexto = {"Motherboards": mother_boards}
    
    return render(request, "GamerTechArg/leermotherboards.html",contexto)


def leer_almacenamiento(request):
    
    storage = Almacenamiento.all()
    contexto = {"Almacenamiento": storage}
    
    return render(request, "GamerTechArg/leeralmacenamiento.html",contexto)


def leer_memoriasram(request):
    
    ram = MemoriasRAM.all()
    contexto = {"Memorias RAM": ram}
    
    return render(request, "GamerTechArg/leermemoriasram.html",contexto)


def leer_procesadores(request):
    
    processors = Procesadores.all()
    contexto = {"Procesadores": processors}
    
    return render(request, "GamerTechArg/leerprocesadores.html",contexto)


def eliminar_placadevideo(request, placa_modelo):
    placa_de_video = PlacasDeVideo.objects.get(modelo=placa_modelo)
    placa_de_video.delete()
    
    placas = PlacasDeVideo.objects.all()
    contexto = {"placas": placas}
    
    return render(request, "GamerTechArg/leerPlacas.html",contexto)


def editar_placasdevideo(request, placa_modelo):
    placa_de_video = PlacasDeVideo.objects.get(modelo=placa_modelo)
    if request.method == 'POST':
        miFormulario=PlacasDeVideoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            placa_de_video.marca=informacion['marca']
            placa_de_video.modelo=informacion['modelo']
            placa_de_video.año=informacion['año']
            placa_de_video.descripcion=informacion['descripcion']
            placa_de_video.precio=informacion['precio']
            
            placa_de_video.save()
            
            return render(request, 'GamerTechArg/inicio.html')
        
    else:
        
        miFormulario = PlacasDeVideoFormulario(initial={'marca':placa_de_video.marca, 'modelo':placa_de_video.modelo, 'año':placa_de_video.año,'descripcion': placa_de_video.descripcion, 'precio':placa_de_video.precio})
        
    return render(request, "GamerTechArg/editarPlaca.html", {"miFormulario": miFormulario, "placa_modelo":placa_modelo})



class PlacasDeVideoListView(ListView):
    model = PlacasDeVideo
    context_object_name = "placasdevideo"
    template_name = "GamerTechArg/placas_lista.html"
    

class PlacasDeVideoDetailView(DetailView):
    model = PlacasDeVideo
    template_name = "GamerTechArg/placas_detalle.html"
    

class PlacasDeVideoCreateView(CreateView):
    model = PlacasDeVideo
    template_name = "GamerTechArg/placas_crear.html"
    success_url = reverse_lazy('ListaPlacas')
    fields = ['marca','modelo','año','descripcion','precio']
    
    
class PlacasDeVideoUpdateView(UpdateView):
    model = PlacasDeVideo
    template_name = "GamerTechArg/placas_editar.html"
    success_url = reverse_lazy('ListaPlacas')
    fields = ['marca','modelo','año','descripcion','precio']
    
    
class PlacasDeVideoDeleteView(DeleteView):
    model = PlacasDeVideo
    template_name = "GamerTechArg/placa_borrar.html"
    success_url = reverse_lazy('ListaPlacas')
    
#MOTHERBOARD
class MotherboardsListView(ListView):
    model = Motherboards
    context_object_name = "motherboards"
    template_name = "GamerTechArg/motherboards_lista.html"
    

class MotherboardsDetailView(DetailView):
    model = Motherboards
    template_name = "GamerTechArg/motherboards_detalle.html"
    

class MotherboardsCreateView(CreateView):
    model = Motherboards
    template_name = "GamerTechArg/motherboards_crear.html"
    success_url = reverse_lazy('ListaMotherboards')
    fields = ['marca','modelo','año','descripcion','precio']
    
    
class MotherboardsUpdateView(UpdateView):
    model = Motherboards
    template_name = "GamerTechArg/motherbards_editar.html"
    success_url = reverse_lazy('ListaMotherboards')
    fields = ['marca','modelo','año','descripcion','precio']
    
    
class MotherboardsDeleteView(DeleteView):
    model = Motherboards
    template_name = "GamerTechArg/motherboards_borrar.html"
    success_url = reverse_lazy('ListaMotherboards')
