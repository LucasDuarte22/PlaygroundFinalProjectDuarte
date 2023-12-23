from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#COMPONENETES:

class PlacasDeVideo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    descripcion =models.CharField(max_length=1000)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.año} - Descripcion: {self.descripcion} - Precio: {self.precio}"
        
        
class Motherboards(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    año = models.IntegerField()
    descripcion =models.CharField(max_length=255)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.anio} - Descripcion: {self.descripcion} - Precio: {self.precio}"
    
    
    
class Almacenamiento(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    descripcion =models.CharField(max_length=255)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.anio} - Descripcion: {self.descripcion} - Precio: {self.precio}"
    
    
class MemoriasRAM(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    descripcion =models.CharField(max_length=255)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.anio} - Descripcion: {self.descripcion} - Precio: {self.precio}"
    
    
class Procesadores(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    descripcion =models.CharField(max_length=255)
    precio = models.IntegerField()
    
    def __str__(self) -> str:
        return f"Marca: {self.marca} - Modelo: {self.modelo} - Año: {self.anio} - Descripcion: {self.descripcion} - Precio: {self.precio}"
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    def __str__(self):
        return f"{self.user} - {self.imagen}"