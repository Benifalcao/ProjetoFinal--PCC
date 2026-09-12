

# Create your views here.
from django.shortcuts import render, redirect
from .models import ObjetoTroca
from .forms import ObjetoTrocaForm


def listar_objetos_troca(request):
    objetos_troca = ObjetoTroca.objects.all()
    return render(request, 'ObjetoTroca/listar_objeto_troca.html', {'objetos_troca': objetos_troca})


def criar_objeto_troca(request):
    if request.method == 'POST':
        form = ObjetoTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ObjetoTroca:listar_objetos_troca')
    else:
        form = ObjetoTrocaForm()
    return render(request, 'ObjetoTroca/criar_objeto_troca.html', {'form': form})