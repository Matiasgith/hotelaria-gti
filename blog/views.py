from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Postagem, Comentario
from .forms import ComentarioForm


def index(request):
    if request.GET.get('pesquisa'):
        pesq = request.GET.get('pesquisa')
        postagens = Postagem.objects.filter(
            Q(titulo__icontains=pesq) | Q(conteudo__icontains=pesq)
        ).order_by('-id').filter(mostrar=True)
    else:
        postagens = Postagem.objects.all().order_by('-id').filter(mostrar=True)
    contexto = {
        'posts': postagens
    }

    return render(request, 'blog/index.html', contexto)

# ------------------------------------------------------------
def ocultos(request):
    if request.GET.get('pesquisa'):
        pesq = request.GET.get('pesquisa')
        postagens = Postagem.objects.filter(
            Q(titulo__icontains=pesq) | Q(conteudo__icontains=pesq)
        ).order_by('-id').filter(mostrar=False)
    else:
        postagens = Postagem.objects.all().order_by('-id').filter(mostrar=False)
    contexto = {
        'posts': postagens
    }
    return render(request, 'blog/ocultos.html', contexto)

# ------------------------------------------------------------
def postagem(request, id_post):
    postagem = get_object_or_404(Postagem, id=id_post)
    comentario = Comentario.objects.all().filter(postagem =id_post).order_by('-id')
    contexto = {
        'post': postagem,
        'comentarios':comentario
    }
    return render(request, 'blog/postagem.html', contexto)
# ------------------------------------------------------------

def edit_postagem(request, id_post):
    postagem = get_object_or_404(Postagem, pk=id_post)
   
    contexto = {
        'post': postagem
    }
    if postagem.mostrar == False:
        messages.error(request, "Não pode acessar essa pagina")
        return render(request, 'blog/postagem.html', contexto)
    elif request.method == "POST":
        # strip() = remover os espaços antes e depois da palavra
        titulo = request.POST.get('titulo').strip()
        conteudo = request.POST.get("conteudo").strip()
        mostrar = request.POST.get('mostrar')
        if titulo == "" or conteudo == "":
            messages.error(request, "Titulo ou conteudo inválidos!")
            return render(request, 'blog/edit_postagem.html', contexto)
        if len(titulo) < 8:
            messages.error(request, "Título muito curto!")
            return render(request, 'blog/edit_postagem.html', contexto)
        if (postagem.mostrar==False):
            # if request == "edit":
            #     ...
            messages.error(request, "Não pode editar postagem oculta")
            return render(request, 'blog/ocultos.html', contexto)
        postagem.titulo = titulo
        postagem.conteudo = conteudo
        postagem.mostrar = mostrar
        postagem.save()
        messages.success(request, "Postagem editada com sucesso!")
        return redirect('index')
    return render(request, 'blog/edit_postagem.html', contexto)

# ------------------------------------------------------------
def add_postagem(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo').strip()
        conteudo = request.POST.get('conteudo').strip()
        mostrar = request.POST.get('mostrar')
        imagem = request.FILES.get('imagem')
        if titulo == "" or conteudo == "":
            messages.error(request, "Titulo ou conteudo inválidos!")
            return render(request, 'blog/add_postagem.html')
        if len(titulo) < 8:
            messages.error(request, "Título muito curto!")
            return render(request, 'blog/add_postagem.html')
        nova_postagem = Postagem()
        nova_postagem.titulo = titulo
        nova_postagem.conteudo = conteudo
        nova_postagem.mostrar = mostrar
        nova_postagem.imagem = imagem
        
        nova_postagem.save()
        messages.success(request, "Postagem salva com sucesso!")
        return redirect('index')
    return render(request, 'blog/add_postagem.html')
# ------------------------------------------------------------

def del_postagem(request, id_post):
    postagem = get_object_or_404(Postagem, pk=id_post)
    contexto = {
        'post': postagem
    }
    if postagem.mostrar == False:
        messages.error(request, "Não pode acessar essa pagina de excluir ocultos")
        return render(request, 'blog/ocultos.html', contexto)
    if request.method == 'POST':
        postagem.delete()
        messages.success(request, "Postagem deletada com sucesso!")
        return redirect('index')
    return render(request, 'blog/del_postagem.html', contexto)
# --------------------------------------------------------------



def add_comentario(request, id_postagem):
    form = ComentarioForm(initial={'postagem': id_postagem})
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Comentarios adicionado com sucesso")
    context = {
        "form": form
        }
    return render(request, 'blog/add_comentario.html', context)

# -------------------------------------------------------------------------

def edit_comentario(request, id_comentario):
    comentario = get_object_or_404(Comentario, pk=id_comentario)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, "Comentário editado com sucesso")
            return redirect('index')
    else:
        form = ComentarioForm(instance=comentario)
    
    context = {
        "form": form,
        "comentarios": comentario
    }
    
    return render(request, 'blog/edit_comentario.html', context)

# -----------------------------------------------------------------------

def del_comentario(request, id_comentario):
    comentario = get_object_or_404(Comentario, pk=id_comentario)
    
    if request.method == 'POST':
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            comentario.delete()
            messages.success(request, "Comentário deletado com sucesso")
            return redirect('index')
    else:
        form = ComentarioForm(instance=comentario)
    
    context = {
        "form": form,
        "comentarios": comentario
    }
    
    return render(request, 'blog/del_comentario.html', context)