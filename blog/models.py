from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()
    data = models.DateField(auto_now_add=True)
    imagem = models.ImageField(upload_to='blog', blank=True, null=True)
    os_choice = (
        ('Informativo', 'Informativo'),
        ('Erótico', 'Erótico'),
        ('Contos', 'Contos'),
        ('Romance', 'Romance'),
    )
    tipo = models.CharField(max_length=30, blank=True, null=True, choices=os_choice)
    autor = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
