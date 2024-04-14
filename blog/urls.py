from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="Blog"),
    #el int para que en la url tome como numero el id
    path('categoria/<int:categoria_id>', views.categoria, name="categoria"),
]
