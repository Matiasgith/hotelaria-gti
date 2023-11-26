from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from reservas.models import Quartos

def quartos(request):
    quartos = Quartos.objects.all()
    contexto={
        'quart': quartos
    }
    return render(request, 'quartos/quartos.html', contexto)


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
            return render(request, 'quartos/cad_quartos.html')
        if not nome or not numero or not valor_diaria or not capacidade or not descricao:
            messages.error(request, "Todos os campos devem ser preenchidos.")
            return render(request, 'quartos/cad_quartos.html')
        if float(valor_diaria) <= 0:
            messages.error(request, "O preço deve ser maior que zero")
            return render(request, 'produtos/quartos.html')
        if int(numero)<= 0 or int(capacidade) <= 0:
            messages.error(request, "O numero deve ser maior que zero")
            return render(request, 'quartos/cad_quartos.html')
        if len(nome) < 7:
            messages.error(request, "nome muito curto!")
            return render(request, 'quartos/cad_quartos.html')
        else:
            novo_quarto = Quartos()
            novo_quarto.nome = nome
            novo_quarto.numero = int(numero)
            novo_quarto.valor_diaria = float(valor_diaria)
            novo_quarto.capacidade = int(capacidade)
            novo_quarto.descricao = descricao
            novo_quarto.ativo = bool(ativo) # Convertendo para booleano

            novo_quarto.save()
            messages.success(request, "Quarto salvo com sucesso!")
            return redirect('quartos')
    return render(request, 'quartos/cad_quartos.html')



def detalhes_quartos(request, id_quarto):
    quartos = get_object_or_404(Quartos, id=id_quarto)
    contexto={
        'quart': quartos
    }
    return render(request, 'quartos/detalhes_quartos.html', contexto)