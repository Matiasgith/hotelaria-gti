from django.contrib import admin
from .models import Quartos, Hospedes

class HospedesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email','data_nasci','cpf', 'telefone', 'cidade','estado']
    list_display_links=['id','nome','email'  ]
    list_per_page = 5
class QuartosAdmin(admin.ModelAdmin):
    list_display=['id', 'nome', 'numero','valor_diaria','capacidade','descricao','ativo']
    list_display_links = ['id', 'nome', 'valor_diaria','capacidade']
    list_per_page = 5


# Register your models here.
admin.site.register(Quartos, QuartosAdmin)
admin.site.register(Hospedes, HospedesAdmin)