from django.urls import path

from . import views


urlpatterns = [
    path('cad_reservas', views.cad_reservas, name='cad_reservas'),
    path('', views.reservas, name='reservas'),
]
