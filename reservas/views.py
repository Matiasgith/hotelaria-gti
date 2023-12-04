from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from reservas.models import Quartos, Hospedes, Reservas 
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def cad_reservas(request):
    # criando as instancias e filtrando quartos por ativo ou não
    quartos = Quartos.objects.all().filter(ativo=True)
    hospedes = Hospedes.objects.all()

    contexto={
        'quart': quartos,
        'hosp': hospedes, 
    }
    
    if request.method == 'POST':
        # Obtenha os dados do formulário
        entrada_prevista = request.POST.get('entrada_prevista')
        saida_prevista = request.POST.get('saida_prevista')
        numero_pessoas = request.POST.get('numero_pessoas')

        # Obtenha os objetos Hospedes e Quartos relacionados
        hospede_id = request.POST.get('hospede_id')
        quarto_id = request.POST.get('quarto_id')
        # Obtenha os objetos Hospedes e Quartos correspondentes
        hospede = Hospedes.objects.get(id=hospede_id)
        quarto = Quartos.objects.get(id=quarto_id)
        

        if not entrada_prevista or not saida_prevista  or not numero_pessoas or not hospede_id or not quarto_id:
        # Tratar erro, talvez redirecionar de volta ao formulário com uma mensagem de erro
            messages.error(request, "Preenxa todos os campos por favor!")
            return render(request, 'reservas/cad_reservas.html')
        if entrada_prevista >= saida_prevista:
            # Garanta que as datas de entrada e saída sejam válidas e que a data de 
            # entrada seja anterior à data de saída:
            messages.error(request, "A data tem que ser maior ou igual a da entrada!")
            return render(request, 'reservas/cad_reservas.html')
        if int(numero_pessoas) <= 0 or int(numero_pessoas) > quarto.capacidade:
            messages.error(request, f"O número de pessoas deve estar entre 1 e {quarto.capacidade} que e a capacidade desse quarto = {quarto.capacidade}")
            return render(request, 'reservas/cad_reservas.html')
        
        else:
            try:#Chekando se os IDs de hóspede e quarto correspondam a registros existentes
                hospede = Hospedes.objects.get(id=hospede_id)
                quarto = Quartos.objects.get(id=quarto_id)
            except Hospedes.DoesNotExist or Quartos.DoesNotExist:
                messages.error(request, "Valores não existem no banco de dados!")
                return render(request, 'reservas/cad_reservas.html')
            
            # Converta as datas para objetos datetime
            entrada_prevista = timezone.datetime.strptime(entrada_prevista, '%Y-%m-%d').date()
            saida_prevista = timezone.datetime.strptime(saida_prevista, '%Y-%m-%d').date()
            # Verifique se o quarto já está reservado para as datas fornecidas
            if Reservas.objects.filter(quartos=quarto_id, entrada_prevista=entrada_prevista, saida_prevista=saida_prevista).exists():
                messages.error(request, "O quarto já está reservado para esse período!")
                return render(request, 'reservas/cad_reservas.html', contexto)
            # Calculo do valor da estadia
            numero_dias = (saida_prevista - entrada_prevista).days
             # Obtenha o valor da diária do quarto (agora corretamente obtendo um único objeto Quartos)
            valor_diaria = quarto.valor_diaria
            valor_estadia = numero_dias * valor_diaria
            # Passe o número máximo de pessoas para o template
            no_reseva = Reservas()
            no_reseva.entrada_prevista = entrada_prevista
            no_reseva.saida_prevista = saida_prevista
            no_reseva.valor_estadia = float(valor_estadia)
            no_reseva.numero_pessoas = int(numero_pessoas)
            no_reseva.hospedes = hospede
            no_reseva.quartos = quarto
            no_reseva.save()
            messages.success(request, "Rserva salva com sucesso!")
            return redirect('reservas')
    
    return render(request, 'reservas/cad_reservas.html', contexto)

@login_required(login_url='login')
def reservas(request):
    reservas = Reservas.objects.all()
    contexto={
        'reserv': reservas        
    }
    
    return render(request, 'reservas/reservas.html', contexto)

@login_required(login_url='login')
def detalhes_reservas(request, id_reservas):
    reservas = get_object_or_404(Reservas, id=id_reservas)
    contexto={
        'reserv': reservas
    }
    return render(request, 'reservas/detalhes_reservas.html', contexto)


@login_required(login_url='login')
def edit_reservas(request, id_reservas):
    reservas = get_object_or_404(Reservas, pk=id_reservas)
    quartos = Quartos.objects.all().filter(ativo=True)
    hospedes = Hospedes.objects.all()
    contexto={
        'reserv': reservas,
        'quart': quartos,
        'hosp': hospedes, 
    }
    
    if request.method == 'POST':
        # Obtenha os dados do formulário
        entrada_prevista = request.POST.get('entrada_prevista')
        saida_prevista = request.POST.get('saida_prevista')
        numero_pessoas = request.POST.get('numero_pessoas')

        # Obtenha os objetos Hospedes e Quartos relacionados
        hospede_id = request.POST.get('hospede_id')
        quarto_id = request.POST.get('quarto_id')
        # Obtenha os objetos Hospedes e Quartos correspondentes
        hospede = Hospedes.objects.get(id=hospede_id)
        quarto = Quartos.objects.get(id=quarto_id)

        if not entrada_prevista or not saida_prevista  or not numero_pessoas or not hospede_id or not quarto_id:
        # Tratar erro, talvez redirecionar de volta ao formulário com uma mensagem de erro
            messages.error(request, "Preenxa todos os campos por favor!")
            return render(request, 'reservas/edit_reservas.html')
        if entrada_prevista >= saida_prevista:
            # Garanta que as datas de entrada e saída sejam válidas e que a data de 
            # entrada seja anterior à data de saída:
            messages.error(request, "A data tem que ser maior ou igual a da entrada!")
            return render(request, 'reservas/edit_reservas.html')
        if int(numero_pessoas) <= 0 or int(numero_pessoas) > quarto.capacidade:
            messages.error(request, f"O número de pessoas deve estar entre 1 e {quarto.capacidade} que e a capacidade desse quarto = {quarto.capacidade}")
            return render(request, 'reservas/edit_reservas.html')
        
        else:
            try:#Chekando se os IDs de hóspede e quarto correspondam a registros existentes
                hospede = Hospedes.objects.get(id=hospede_id)
                quarto = Quartos.objects.get(id=quarto_id)
            except Hospedes.DoesNotExist or Quartos.DoesNotExist:
                messages.error(request, "Valores não existem no banco de dados!")
                return render(request, 'reservas/edit_reservas.html')
            
            # Converta as datas para objetos datetime
            entrada_prevista = timezone.datetime.strptime(entrada_prevista, '%Y-%m-%d').date()
            saida_prevista = timezone.datetime.strptime(saida_prevista, '%Y-%m-%d').date()

            # Calculo do valor da estadia
            numero_dias = (saida_prevista - entrada_prevista).days
             # Obtenha o valor da diária do quarto (agora corretamente obtendo um único objeto Quartos)
            valor_diaria = quarto.valor_diaria
            valor_estadia = numero_dias * valor_diaria
            # Passe o número máximo de pessoas para o template

            reservas.entrada_prevista = entrada_prevista
            reservas.saida_prevista = saida_prevista
            reservas.valor_estadia = float(valor_estadia)
            reservas.numero_pessoas = int(numero_pessoas)
            reservas.hospedes = hospede
            reservas.quartos = quarto
            reservas.save()
            messages.success(request, "Rserva editada com sucesso!")
            return redirect('reservas')

    return render(request, 'reservas/edit_reservas.html', contexto)

@login_required(login_url='login')
def del_reservas(request, id_reservas):
    reservas = get_object_or_404(Reservas, pk=id_reservas)
    quartos = Quartos.objects.all().filter(ativo=True)
    hospedes = Hospedes.objects.all()

    contexto={
        'reserv': reservas,
        'quart': quartos,
        'hosp': hospedes, 
    }
    if request.method == 'POST':
        
        reservas.delete()
        messages.success(request, "Reserva deletado com sucesso!")
        return redirect('reservas')
    return render(request, 'reservas/del_reservas.html', contexto)