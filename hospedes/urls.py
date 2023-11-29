from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='hos_index'),
    path('hospedes/cadastro/', views.cad_hospedes, name='cad_hospedes'),
    path('hospedes/detalhes/<int:hospede_id>', views.hos_detalhes, name='hos_detalhes'),
    path('hospedes/editar/<int:hospede_id>', views.hos_editar, name='hos_editar'),
    path('hospedes/excluir/<int:hospede_id>', views.hos_excluir, name='hos_excluir'), 
]
