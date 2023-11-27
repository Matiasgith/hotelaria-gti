from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from reservas.models import Hospedes
from django.db.models import Q
from datetime import datetime

def index(request):
    return render(request, 'hospedes/index.html')

def cad_hospedes(request):
     
     if request.method == 'POST':
        nome = request.POST.get('nome')
        email= request.POST.get('email')
        data_nasci = request.POST.get('data_nasci')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone') 
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        data_nasci = datetime.strptime(data_nasci, '%d/%m/%Y').strftime('%Y-%m-%d')

        if nome is None or len(nome) < 3 or nome.isspace():
            messages.error(request, "Muito curto!")
            return render(request,'hospedes/cadastro_hospedes.html')
        
        if cpf is None or len(cpf) < 11 or cpf.isspace():
            messages.error(request, "CPF inválido!")
            return render(request,'hospedes/cadastro_hospedes.html')
               
        if telefone is None or len(telefone) < 10 or telefone.isspace():
            messages.error(request, "Telefone inválido!")
            return render(request,'hospedes/cadastro_hospedes.html')
        
        novo_hospede = Hospedes(nome=nome, email=email, data_nasci=data_nasci, cpf=cpf, telefone=telefone, cidade=cidade, estado=estado)
        novo_hospede.save()
        messages.success(request,"Hospede salvo com sucesso!")
        return redirect(request,'hos_index')
     
     return render(request, 'hospedes/cadastro_hospedes.html')

def hos_lista(request):
    return render(request, 'hospedes/index.html')