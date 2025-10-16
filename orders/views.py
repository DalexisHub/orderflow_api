from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Client, Order
from .serializers import ClientSerializer, OrderSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('cliente').all()
    serializer_class = OrderSerializer
    filter_backends = [SearchFilter]
    search_fields = ['estado', 'cliente__nombre']