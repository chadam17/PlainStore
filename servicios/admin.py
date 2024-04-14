from django.contrib import admin
from .models import Servicio

# Register your models here.

#clase para que los campos created y updated aparezcan en BBDD
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio, ServicioAdmin)