from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from reservas.models import Quartos

def quartos(request):

    return render(request, 'quartos/quartos.html')




def cad_quartos(request):
    if request.method == 'POST':
        nome = request.POST.get('nome').strip()
        numero = request.POST.get('numero')
        valor_diaria = request.POST.get('valor_diaria')
        capacidade = request.POST.get('capacidade')
        descricao = request.POST.get('descricao').strip()
        ativo = request.POST.get('ativo')
        if nome == "" or numero == "" or valor_diaria =="" or capacidade =="" or descricao == "":
                messages.error(request, "Nome ou conteudo inválidos!")
                return render(request, 'produtos/quartos.html')
        else:
            novo_quarto = Quartos()
            novo_quarto.nome = nome
            novo_quarto.numero = numero
            novo_quarto.valor_diaria = float(valor_diaria)
            novo_quarto.capacidade = capacidade
            novo_quarto.descricao = descricao
            novo_quarto.ativo = bool(ativo) # Convertendo para booleano

            novo_quarto.save()
            messages.success(request, "Quarto salvo com sucesso!")
            return redirect('quartos')
    return render(request, 'quartos/cad_quartos.html')