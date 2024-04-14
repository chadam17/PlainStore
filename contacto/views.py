from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    # para rescatar la informacion introducida en el formulario
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde Django", "El usuario con nombre {} con la dirección {} says:\n\n {}".format(nombre,email,contenido), "", ["cmbld17@gmail.com"], reply_to=[email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?noValido")
            #para que redireccione a una url de confirmacion de datos de formulario correctos
            

    return render(request, "contacto/contacto.html", {"miFormulario": formulario_contacto})
