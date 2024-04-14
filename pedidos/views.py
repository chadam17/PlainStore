from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from pedidos.models import LineaPedido, Pedido
from carro.carro import Carro
from carro.context_processor import importe_total_carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# Create your views here.

#decorador
@login_required(login_url = "/autenticacion/logear")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user = request.user)
    carro = Carro(request)
    lineas_pedido = list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido = pedido,
        lineas_pedido = lineas_pedido,
        nombreusuario = request.user.username,
        emailusuario = request.user.email,
        #total = carro.importe_total_carro(request)
    )

    messages.success(request, "Delivery in progress")

    return redirect("../tienda")

#**kwargs es porque desconocemos el numero de parametros y puede variar mas adelante
def enviar_mail(**kwargs):

    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario")
    })

    #para que no devuelva etiquetas y caracteres html que puedan haber en la variable mensaje
    mensaje_texto = strip_tags(mensaje)
    from_email = "cmbld17@gmail.com"
    #comentamos porque en BBDD hay algun usuario con email valido
    #to = kwargs.get("emailusuario")
    to = "cmbld17@gmail.com"
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)
