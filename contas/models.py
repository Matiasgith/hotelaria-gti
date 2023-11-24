from django.db import models

class Contas(models.Model):
    nome = models.CharField(max_length=10, blank=False)
    sobrenome = models.CharField(max_length=20, blank=False)
    email= models.EmailField(max_length=40, blank=False)
    usuario = models.CharField(max_length=40, blank=False)
    senha = models.CharField(max_length=40, blank=False)
    repetirsenha = models.CharField(max_length=40, blank=False)

def __str__(self):
    return self.name
