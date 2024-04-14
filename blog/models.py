from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    #posts = models.ManyToManyField(Post)
    posts = None
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # los atributos null y blank para indicar que puede no haber imagen asociada al Post
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    #requiere el import de User, decimos que si se borra el autor del Post, se borrará todo lo asociado en cascada
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #establecemos la relacion con la clase Categoria
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo
    
Categoria.posts = models.ManyToManyField(Post)
