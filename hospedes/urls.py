from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='hos_index'),
    path('hospedes/cadastro/', views.cad_hospedes, name='cad_hospedes'),
    path('hospedes/detalhes/<int:Hospede_id>', views.hos_detalhes, name='hos_detalhes'), 
]