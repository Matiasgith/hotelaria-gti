from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from reservas.models import Hospedes
from django.db.models import Q
from datetime import datetime
from dateutil import parser
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    hospede = Hospedes.objects.all()
    contexto={
        'hosp': hospede}
    return render(request, 'hospedes/index.html', contexto)

@login_required(login_url='login')
def cad_hospedes(request):
     
     if request.method == 'POST':
        nome = request.POST.get('nome')
        email= request.POST.get('email')
        data_nasci = request.POST.get('data_nasci')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone') 
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        if  nome == '' or  email=='' or  data_nasci=='' or cpf=='' or  telefone== '' or cidade=='' or  estado=='':
            messages.error(request, "Dados inválidos !")
            return render(request, 'hospedes/cadastro_hospedes.html')
        
        # data_nasci = datetime.strptime(data_nasci, '%d/%m/%Y').strftime('%Y-%m-%d')
        data_nasci = timezone.datetime.strptime(data_nasci, '%Y-%m-%d').date()

        if nome is None or len(nome) < 3 or nome.isspace():
            messages.error(request, "Muito curto!")
            return render(request,'hospedes/cadastro_hospedes.html')
        
        if cpf is None or len(cpf) < 11 or cpf.isspace():
            messages.error(request, "CPF inválido!")
            return render(request,'hospedes/cadastro_hospedes.html')
        
        if Hospedes.objects.filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado!")
            return render(request, 'hospedes/cadastro_hospedes.html')
        
        if Hospedes.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado!")
            return render(request, 'hospedes/cadastro_hospedes.html')

        if telefone is None or len(telefone) < 10 or telefone.isspace():
            messages.error(request, "Telefone inválido!")
            return render(request,'hospedes/cadastro_hospedes.html')
        
        novo_hospede = Hospedes(nome=nome, email=email, data_nasci=data_nasci, cpf=cpf, telefone=telefone, cidade=cidade, estado=estado)
        novo_hospede.save()
        messages.success(request,"Hospede salvo com sucesso!")
        return redirect('hos_index')
     
     return render(request, 'hospedes/cadastro_hospedes.html')


@login_required(login_url='login')
def hos_detalhes(request, hospede_id):
    hospede = get_object_or_404(Hospedes, id=hospede_id)
    contexto={
        'hospede': hospede
    }
    return render(request, 'hospedes/detalhes_hospedes.html', contexto)


@login_required(login_url='login')
def hos_editar(request, hospede_id):
    hospede = get_object_or_404(Hospedes, pk=hospede_id)

    if request.method == 'POST':
        
        nome = request.POST.get('nome')
        email= request.POST.get('email')
        data_nasci = request.POST.get('data_nasci')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone') 
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        if  nome == '' or  email=='' or  data_nasci=='' or cpf=='' or  telefone== '' or cidade=='' or  estado=='':
            messages.error(request, "Dados inválidos !")
            return render(request, 'hospedes/cadastro_hospedes.html')
        
        # data_nasci = datetime.strptime(data_nasci, '%d/%m/%Y').strftime('%Y-%m-%d')
        data_nasci = timezone.datetime.strptime(data_nasci, '%Y-%m-%d').date()

        if nome is None or len(nome) < 3 or nome.isspace():
            messages.error(request, "Muito curto!")
            return render(request,'hospedes/cadastro_hospedes.html')
        
        if cpf is None or len(cpf) < 11 or cpf.isspace():
            messages.error(request, "CPF inválido!")
            return render(request,'hospedes/cadastro_hospedes.html')
        
        if Hospedes.objects.exclude(pk=hospede_id).filter(cpf=cpf).exists():
            messages.error(request, "CPF já cadastrado em outro hospede!")
            return render(request, 'hospedes/cadastro_hospedes.html')
        
        if Hospedes.objects.filter(email=email).exclude(pk=hospede_id).exists():
            messages.error(request, "E-mail já cadastrado!")
            return render(request, 'hospedes/cadastro_hospedes.html')

        if telefone is None or len(telefone) < 10 or telefone.isspace():
            messages.error(request, "Telefone inválido!")
            return render(request,'hospedes/cadastro_hospedes.html')
        hospede.nome = nome
        hospede.email = email
        hospede.data_nasci = data_nasci
        hospede.cpf = cpf
        hospede.telefone = telefone
        hospede.cidade = cidade
        hospede.estado = estado
        hospede.save()
        messages.success(request, "Hospede editado com sucesso!")
        return redirect('hos_index')
    return render(request, 'hospedes/editar_hospedes.html', {'hospede': hospede})


@login_required(login_url='login')
def hos_excluir(request, hospede_id):
    hospedes = get_object_or_404(Hospedes, pk=hospede_id)

    contexto = {
        'hospede': hospedes
    }

    if request.method == 'POST':
        hospedes.delete()
        messages.success(request, "Hospede deletado com sucesso!")
        return redirect('hos_index')
    return render(request, 'hospedes/del_hospedes.html', contexto)
