from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from reservas.models import Quartos, Hospedes, Reservas 

# Create your views here.


def home(request):
    reservas = Reservas.objects.all()
    contexto={
        'reserv': reservas        
    }
    
    return render(request, 'home/home_hotelaria.html', contexto)
