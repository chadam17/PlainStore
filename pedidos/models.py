from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Producto
from django.db.models import F, Sum, FloatField

# Create your models here.

#nos devuelve el usuario activo (el que se ha logeado)
User = get_user_model()

class Pedido(models.Model):
    #si se elimina el usuario con el todo lo relacionado
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.id
    
    #decorador total del pedido completo
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total = sum(F("precio")*F("cantidad"), output_field = FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # la f es para dar formato
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'Linea Pedidos'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']
