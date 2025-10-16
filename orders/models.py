from django.db import models

class Client(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.nombre


class Order(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('enviado', 'Enviado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Client, related_name='orders', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre} - {self.estado}"