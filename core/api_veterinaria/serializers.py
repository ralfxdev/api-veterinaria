from urllib import response
from rest_framework import serializers
from api_veterinaria import models
from api_veterinaria.models import Cliente, Personal, Animal, Diagnostico, ElementoFactura, Factura

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['cliente'] = instance.cliente.nombre + ' ' + instance.cliente.apellidos
        return response

class DiagnosticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnostico
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['animal'] = instance.animal.nombre + ' ' + instance.animal.tipo
        response['personal'] = instance.personal.nombre + ' ' + instance.personal.apellidos
        return response

class ElementoFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementoFactura
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['diagnostico'] = instance.diagnostico.descripcion
        return response

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['elemento_factura'] = ElementoFacturaSerializer(instance.elemento_factura.all(), many=True).data
        return response
