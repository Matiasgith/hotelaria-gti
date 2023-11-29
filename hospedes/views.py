from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from reservas.models import Hospedes
from django.db.models import Q
from datetime import datetime
from dateutil import parser


def index(request):
    hospede = Hospedes.objects.all()
    contexto={
        'hosp': hospede}
    return render(request, 'hospedes/index.html', contexto)


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
        return render(request,'hospedes/index.html')
     
     return render(request, 'hospedes/cadastro_hospedes.html')

def hos_detalhes(request, hospede_id):
    hospede = get_object_or_404(Hospedes, id=hospede_id)
    contexto={
        'hospede': hospede
    }
    return render(request, 'hospedes/detalhes_hospedes.html', contexto)

def hos_editar(request, hospede_id):
    hospede = get_object_or_404(Hospedes, pk=hospede_id)

    if request.method == 'POST':
        hospede.nome = request.POST.get('nome')
        hospede.email = request.POST.get('email')
        hospede.data_nasci = parser.parse(request.POST.get('data_nasci')).date()
        hospede.cpf = request.POST.get('cpf')
        hospede.telefone = request.POST.get('telefone')
        hospede.cidade = request.POST.get('cidade')
        hospede.estado = request.POST.get('estado')

        hospede.save()
        return redirect('hos_index')

    return render(request, 'hospedes/editar_hospedes.html', {'hospede': hospede})