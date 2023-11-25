from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q

def index(request):
    return render(request, 'hospedes/index.html')

def hos_lista(request):
    return render(request, 'hospedes/hospedes_lista.html')