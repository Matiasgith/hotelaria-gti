from django.db import models
from django.utils import timezone
# Create your models here.


class Postagem(models.Model):
    titulo = models.CharField(max_length=20)
    conteudo = models.TextField(max_length=50)
    mostrar = models.BooleanField(default=True, blank=True, null=True)
    imagem = models.ImageField(upload_to='%Y/%m', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Postagens"

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    texto = models.TextField(max_length=50)
    data = models.DateField(default=timezone.now)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto
    
