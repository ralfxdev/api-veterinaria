import this
from weakref import proxy
from django.db import models
from django.forms import CharField

# Create your models here.

"""Creamos nuestras tablas"""

class Persona(models.Model):
    nombre = models.CharField(max_length=75)
    apellidos = models.CharField(max_length=55)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.nombre}' + f' - ' + f'{self.apellidos}'

class Cliente(Persona):
    email = models.EmailField(max_length=75)
    direccion = models.CharField(max_length=75)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.nombre}' + f' - ' + f'{self.apellidos}'

class Personal(Persona):
    fecha_contratacion = models.DateField()

    def __str__(self):
        return f'{self.nombre}' + f' - ' + f'{self.apellidos}'

class Animal(models.Model):
    tipo = models.CharField(max_length=75)
    nombre = models.CharField(max_length=75)
    edad = models.CharField(max_length=75)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}' + f' - ' + f'{self.tipo}'

class Diagnostico(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=75)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.descripcion}'

class ElementoFactura(models.Model):
    elemento = models.CharField(max_length=75)
    precio = models.FloatField()
    catidad = models.IntegerField()
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.elemento}' + f' - ' + f'{self.diagnostico}'

class Factura(models.Model):
    ref_factura = models.CharField(max_length=75)
    elemento_factura = models.ManyToManyField(ElementoFactura)

    def __str__(self):
        return f'{self.ref_factura}'