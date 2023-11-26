from django.contrib import admin
from reservas.models import Hospedes

class HosprdesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'data_nasci', 'cpf', 'telefone', 'cidade', 'estado' ]
    list_display_links = ['id', 'nome']
    list_editable = ['email','cpf', 'telefone', 'cidade', 'estado']
    list_per_page = 5

    def __str__(self):
        return self.nome

admin.site.register(Hospedes)