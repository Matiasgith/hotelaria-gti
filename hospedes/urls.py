from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='hos_index'),
    path('hospedes/cadastro/', views.cad_hospedes, name='cad_hospedes'),
    path('hospedes/lista/', views.hos_lista, name='hos_lista'),
]