from rest_framework import serializers
from .models import Client, Order

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'nombre', 'direccion']


class OrderSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='cliente.nombre', read_only=True)
    client_address = serializers.CharField(source='cliente.direccion', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'cliente', 'client_name', 'client_address', 'fecha', 'monto_total', 'estado']