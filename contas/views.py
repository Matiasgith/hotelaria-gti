from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from .forms import UserForm, UserEditForm
from django.contrib.auth.models import User
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from rolepermissions.roles import assign_role


def cadastro(request): # criação de usuário
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)  # não salvar o usuário no BD
        user.is_active = False  # modificar usuário antes de salvar o usuário
        user.save()
        return redirect('login')
    contexto = {
        'form': form
    }
        
    return render(request, 'contas/cadastro.html', contexto)


def login(request):
    form = AuthenticationForm(request, request.POST or None)
    if form.is_valid():
        auth.login(request, form.get_user())
    contexto = {
        'form': form
    }

    return render(request, 'contas/login.html',contexto)



def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Usuário deslogado!')
    return redirect('login')

def edit_user(request):
    form = UserEditForm(request.POST or None,
                        request.FILES or None,
                        instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            last_pass = form.cleaned_data['last_password']
            if not auth.authenticate(request, username=request.user, password=last_pass):
                messages.error(request, "Antiga senha incorreta!")
                return redirect('edit_user')
            user = form.save(commit=False)
            email_existe = User.objects.exclude(username=request.user).filter(
                email=user.email).exists()
            if email_existe:
                messages.error(request, "Email já existe!")
                return redirect('edit_user')
            user.save(update_fields=['first_name',
                      'last_name', 'email', 'password'])
            messages.success(request, "Usuário editado com sucesso!")
            return redirect('home')
    contexto = {
        'form': form
    }
    return render(request, 'contas/cadastro.html', contexto)