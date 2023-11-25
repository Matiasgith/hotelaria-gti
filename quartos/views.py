from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q


def quartos(request):

    return render(request, 'quartos/quartos.html')

def cad_quartos(request):

    return render(request, 'quartos/cad_quartos.html')