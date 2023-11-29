from django.urls import path

from . import views


urlpatterns = [
    path('', views.quartos, name='quartos'),
    path('cad_quartos/', views.cad_quartos, name='cad_quartos'),
    path('detalhes_quartos/<int:id_quarto>/', views.detalhes_quartos, name='detalhes_quartos'),
    path('edit_quartos/<int:id_quarto>/', views.edit_quartos, name='edit_quartos'),
    path('del_quartos/<int:id_quarto>/', views.del_quartos, name='del_quartos'),
]
