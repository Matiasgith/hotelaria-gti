from django.urls import path

from . import views


urlpatterns = [
    path('cad_reservas', views.cad_reservas, name='cad_reservas'),
    path('', views.reservas, name='reservas'),
    path('detalhes_reservas/<int:id_reservas>/', views.detalhes_reservas, name='detalhes_reservas'),
    path('edit_reservas/<int:id_reservas>/', views.edit_reservas, name='edit_reservas'),
    path('del_reservas/<int:id_reservas>/', views.del_reservas, name='del_reservas'),
]
