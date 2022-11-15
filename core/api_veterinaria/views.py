from sre_constants import ANY_ALL
from django.shortcuts import render
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework import viewsets

#filters
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from api_veterinaria import models
from api_veterinaria.models import Cliente, Personal, Animal, Diagnostico, ElementoFactura, Factura

from api_veterinaria import serializers
from api_veterinaria.serializers import ClienteSerializer, PersonalSerializer, AnimalSerializer, DiagnosticoSerializer, ElementoFacturaSerializer, FacturaSerializer

class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

    def destroy(self, request, *args, **kwargs):
        cliente = self.get_object()
        cliente.delete()

        return Response({"mensaje": "Cliente deleted"})
    
    def put(self, request, *args, **kwargs):
        cliente = self.get_object()
        datos_cliente = request.data

        cliente.nombre = datos_cliente['nombre']
        cliente.apellidos = datos_cliente['apellidos']
        cliente.email = datos_cliente['email']
        cliente.direccion = datos_cliente['direccion']
        cliente.telefono = datos_cliente['telefono']

        cliente.save()

        serializer_class = ClienteSerializer(cliente)

        return Response(serializer_class.data)


class PersonalView(viewsets.ModelViewSet):
    serializer_class = PersonalSerializer
    queryset = Personal.objects.all()

    def destroy(self, request, *args, **kwargs):
        personal = self.get_object()
        personal.delete()

        return Response({"mensaje": "Personal deleted"})
    
    def put(self, request, *args, **kwargs):
        personal = self.get_object()
        datos_personal = request.data

        personal.nombre = datos_personal['nombre']
        personal.apellidos = datos_personal['apellidos']
        personal.fecha_contratacion = datos_personal['fecha_contratacion']

        personal.save()

        serializer_class = PersonalSerializer(personal)

        return Response(serializer_class.data)

class AnimalView(viewsets.ModelViewSet):
    serializer_class = AnimalSerializer
    queryset = Animal.objects.all()

    def destroy(self, request, *args, **kwargs):
        animal = self.get_object()
        animal.delete()

        return Response({"mensaje": "Animal deleted"})
    
    def put(self, request, *args, **kwargs):
        animal = self.get_object()
        datos_animal = request.data

        animal.tipo = datos_animal['tipo']
        animal.nombre = datos_animal['nombre']
        animal.edad = datos_animal['edad']
        animal.cliente = datos_animal['cliente']

        animal.save()

        serializer_class = AnimalSerializer(animal)

        return Response(serializer_class.data)

class DiagnosticoView(viewsets.ModelViewSet):
    serializer_class = DiagnosticoSerializer
    queryset = Diagnostico.objects.all()

    def destroy(self, request, *args, **kwargs):
        diagnostico = self.get_object()
        diagnostico.delete()

        return Response({"mensaje": "Diagnostico deleted"})
    
    def put(self, request, *args, **kwargs):
        diagnostico = self.get_object()
        datos_diagnostico = request.data

        diagnostico.fecha = datos_diagnostico['fecha']
        diagnostico.descripcion = datos_diagnostico['descripcion']
        diagnostico.animal = datos_diagnostico['animal']
        diagnostico.personal = datos_diagnostico['personal']

        diagnostico.save()

        serializer_class = DiagnosticoSerializer(diagnostico)

        return Response(serializer_class.data)


class ElementoFacturaView(viewsets.ModelViewSet):
    serializer_class = ElementoFacturaSerializer
    queryset = ElementoFactura.objects.all()

    def destroy(self, request, *args, **kwargs):
        elemento_factura = self.get_object()
        elemento_factura.delete()

        return Response({"mensaje": "ElementoFactura deleted"})
    
    def put(self, request, *args, **kwargs):
        elemento_factura = self.get_object()
        datos_elemento_factura = request.data

        elemento_factura.elemento = datos_elemento_factura['elemento']
        elemento_factura.precio = datos_elemento_factura['precio']
        elemento_factura.catidad = datos_elemento_factura['catidad']
        elemento_factura.diagnostico = datos_elemento_factura['diagnostico']

        elemento_factura.save()

        serializer_class = ElementoFacturaSerializer(elemento_factura)

        return Response(serializer_class.data)

class FacturaView(viewsets.ModelViewSet):
    serializer_class = FacturaSerializer
    queryset = Factura.objects.all()

    def destroy(self, request, *args, **kwargs):
        factura = self.get_object()
        factura.delete()

        return Response({"mensaje": "Factura deleted"})
    
    def put(self, request, *args, **kwargs):
        factura = self.get_object()
        datos_factura = request.data

        factura.ref_factura = datos_factura['ref_factura']
        factura.elemento_factura = datos_factura['elemento_factura']

        factura.save()

        serializer_class = FacturaSerializer(factura)

        return Response(serializer_class.data)

#Animales por nombre

class AnimalesNombreList(generics.ListAPIView):
    serializer_class = AnimalSerializer
    def get_queryset(self):
        queryset = Animal.objects.all()
        nombre = self.request.query_params.get('nombre')
        if nombre is not None:
            queryset = queryset.filter(nombre__icontains=nombre)
        return queryset


#Diagnosticos por fecha

class DiagnosticoFechaList(generics.ListAPIView):
    serializer_class = DiagnosticoSerializer
    def get_queryset(self):
        queryset = Diagnostico.objects.all()
        fecha = self.request.query_params.get('fecha')
        if fecha is not None:
            queryset = queryset.filter(fecha__icontains=fecha)
        return queryset

#Diagnostico por nombre de animal

class DiagnosticoAnimalNombre(generics.ListAPIView):
    serializer_class = DiagnosticoSerializer
    def get_queryset(self):
        queryset = Diagnostico.objects.all()
        nombre = self.request.query_params.get('nombre')
        if nombre is not None:
            queryset = queryset.filter(animal__nombre__icontains=nombre)
        return queryset

#Facturas por id

class FacturaIdList(generics.ListAPIView):
    serializer_class = FacturaSerializer
    def get_queryset(self):
        queryset = Factura.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id__icontains=id)
        return queryset