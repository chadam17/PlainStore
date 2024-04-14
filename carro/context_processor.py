from .carro import Carro
from django.shortcuts import render

def importe_total_carro(request):

    total = 0
    #el precio total del carro solo se actualizará si se ha iniciado sesion, de lo contrario mostrará total = 0€
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total + float(value["precio"])
    else:
        total = "Debes logearte"
        
    return ({"importe_total_carro": total})    
    #return render(request, "tienda/tienda.html" , {"carro": carro, "importe_total_carro": total})
