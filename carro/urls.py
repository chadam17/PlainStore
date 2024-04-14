from django.urls import path
from . import views

#agregamos un namespace para que tenemos en otra aplicacion rutas con los mismos nombres evitamos una colision
app_name="carro"

urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    path("limpiar/<int:producto_id>/", views.limpiar_carro, name="limpiar"),
]
