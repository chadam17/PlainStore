from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, HttpResponse

# Create your views here.

class VRegistro(View):

    def get(self, request):
        #UserCreationForm nos genera un formulario predefinido bastante completo
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        #la informacion del usuario se guarda en la tabla auth_user en BBDD
        #si el registro fue correctamente
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Home')
        #si falló la validacion del formulario
        else:
            #muestra el mensaje de error por cada error
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "registro/registro.html", {"form": form})
        
def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario, password = contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('Home')
            else:
                messages.error(request, "Usuario inválido")
        else:
            #muestra el mensaje de error por cada error
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])     

    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})
    

'''
def logear(request):
    title = "Login"
    form = AuthenticationForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)      
        if user is not None:
          login(request, user)
          return redirect('Home')
          #return HttpResponse("Logged in")
    return render(request, "login/login.html", {"form":form, "title": title})
'''

'''
def logear(request):
    form = AuthenticationForm(request.post)
    
    cd = form.cleaned_data
    user = authenticate(username=cd['username'],
            password=cd['password'])
    if user is not None:
        if user.is_active:
            login(request, user)
            #return HttpResponse('Authenticated ' \
            #       'successfully')
            return redirect('Home')
        else:
            return HttpResponse('Disabled account')


    return render(request, 'registration/login.html', {'form': form})
'''
'''
class VLogin(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login/login.html", {"form:": form})
    
    def post(self, request):
        form = AuthenticationForm()
        return render(request, "login/login.html", {"form:": form})
'''
