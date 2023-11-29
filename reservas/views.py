from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from reservas.models import Quartos, Hospedes, Reservas 

def cad_reservas(request):
    if request.method == 'POST':
        # Obtenha os dados do formulário
        entrada_prevista = request.POST.get('entrada_prevista')
        saida_prevista = request.POST.get('saida_prevista')
        valor_estadia = request.POST.get('valor_estadia')
        numero_pessoas = request.POST.get('numero_pessoas')

        # Obtenha os objetos Hospedes e Quartos relacionados
        hospede_id = request.POST.get('hospede_id')
        quarto_id = request.POST.get('quarto_id')
        hospede = Hospedes.objects.get(id=hospede_id)
        quarto = Quartos.objects.get(id=quarto_id)
    
    return render(request, 'reservas/cad_reservas.html')

def reservas(request):
    
    
    return render(request, 'reservas/reservas.html')