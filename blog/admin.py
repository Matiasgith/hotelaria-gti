from django.contrib import admin

from .models import Postagem, Comentario


class PostagemAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'conteudo']
    list_display_links = ['id', 'titulo']
    list_editable = ['conteudo']
    list_per_page = 5


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'texto', 'data','postagem']
    list_display_links = ['id']
    list_per_page = 10

# # Register your models here.
admin.site.register(Postagem, PostagemAdmin)
admin.site.register(Comentario, ComentarioAdmin)
