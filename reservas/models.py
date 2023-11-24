from django.db import models
from django.utils import timezone

# Create your models here.

class Hospedes(models.Model):
    nome = models.CharField(max_length=30)
    email= models.EmailField(max_length=100, blank=False, unique=True)
    data_nasci = models.DateField(auto_now=False, auto_now_add=False) #O formato padrão para armazenamento é "YYYY-MM-DD".
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nome
    
    class Meta:
      verbose_name_plural = "Hospedes"
    
class Quartos(models.Model):
    nome = models.CharField(max_length=30)
    numero = models.IntegerField(max_length=10)
    valor_diaria = models.FloatField(max_length=30)
    capacidade = models.IntegerField(max_length=10)
    descricao = models.TextField(max_length=150)
    ativo = models.BooleanField(default=True, blank=True, null=True)


    def __str__(self):
        return self.nome
    
    class Meta:
      verbose_name_plural = "Quartos"


class Reservas(models.Model):
    nome = models.CharField(max_length=30)
    entrada_prevista = models.DateField(auto_now=False, auto_now_add=False) #O formato padrão para armazenamento é "YYYY-MM-DD".
    saida_prevista = models.DateField(auto_now=False, auto_now_add=False) #O formato padrão para armazenamento é "YYYY-MM-DD".
    quarto_disponivel = models.CharField(max_length=40)
    valor_estadia = models.FloatField(max_length=30)
    numero_pessoas = models.IntegerField(max_length=10)
    hospedes = models.ForeignKey(Hospedes, on_delete=models.DO_NOTHING)
    quartos = models.ForeignKey(Quartos, on_delete=models.DO_NOTHING)


    def __str__(self):
            return self.nome
    
    class Meta:
      verbose_name_plural = "Reservas"


