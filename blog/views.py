from django.shortcuts import render
from blog.models import Post, Categoria
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def blog(request):
    posts = Post.objects.all()

    categorias_posts = Categoria.objects.all().values_list('id','nombre')
    categorias_posts = list(categorias_posts)
    
#   convertir el QuerySet a list(), el atributo flat se pone si recogemos un unico atributo 
    lista_categorias = Post.objects.all().values_list('categorias', flat=True)   
#   eliminar categorias duplicadas 
    lista_categorias = list(dict.fromkeys(lista_categorias))

    categorias_posts_2 = list(categorias_posts)
    for x in categorias_posts_2:
        if x[0] not in lista_categorias:
            categorias_posts.remove(x)

    return render(request, "blog/blog.html", {"posts": posts, "categorias": categorias_posts})
    #return HttpResponse(template.render(context, request)) 

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    #para que aparezcan los posts filtrados por categoria
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria': categoria, "posts": posts})
