from django.urls import path

from . import views


urlpatterns = [
    path('', views.quartos, name='quartos'),
    path('cad_quartos', views.cad_quartos, name='cad_quartos'),
]
