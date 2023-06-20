from django.shortcuts import render
from .models import Colheitas

def home(request):
    return render(request, 'colheitas/home.html')

def colheitas(request):
    nova_colheita = Colheitas()
    nova_colheita.cultura = request.POST.get('cultura')
    nova_colheita.data_plantio = request.POST.get('datap')
    nova_colheita.data_colheita = request.POST.get('datac')
    nova_colheita.quantidade_colhida = request.POST.get('qtd')
    nova_colheita.save()

    colheitas = {
        'colheitas': Colheitas.objects.all()
    }

    return render(request, 'colheitas/colheitas.html',colheitas)