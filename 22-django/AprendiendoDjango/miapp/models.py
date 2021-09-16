from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    public = models.BooleanField(verbose_name="Público")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created_at']

    def __str__(self):
        if self.public == True:
            publico = "(Publicado)"
        else:
            publico = "(Privado)"

        return f"{self.title} - {publico}"

class Category(models.Model):
    name = models.CharField(max_length=110)
    description = models.CharField(max_length=250)
    created_at = models.DateField()

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"