from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Contas

def login(request):
    if request.method =="POST":
        nomeLogin = request.POST.get('usuario')
        senhaLogin = request.POST.get('senha')
        contas = Contas.objects.all().filter(usuario=nomeLogin, senha=senhaLogin).first()
        if nomeLogin == "" or senhaLogin == "":
            messages.error(request,"Informações inválidas")
            return redirect('login')
        if contas:
            messages.success(request, "Login efetuado com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Nome de usuário ou senha incorretos")
            return redirect('login')
            
    return render(request, 'contas/login.html')

def cadastro(request):
    if request.method =='POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        usuario = request.POST.get('usuario_cad')
        senha = request.POST.get('senha_cad')
        repetirsenha = request.POST.get('repetir_senha')
        if nome == "" or sobrenome == '' or email== '' or usuario =='' or senha =='':
            messages.error(request, "Informações inválidas!")
        novo_usuario = Contas()
        novo_usuario.nome = nome
        novo_usuario.sobrenome = sobrenome
        novo_usuario.email =email
        novo_usuario.usuario = usuario
        novo_usuario.senha =senha
        novo_usuario.repetirsenha =repetirsenha

        novo_usuario.save()
        messages.success(request, "Usuário cadastrado com sucesso!")
        return redirect('login')
            
    return render(request, 'contas/cadastro.html')