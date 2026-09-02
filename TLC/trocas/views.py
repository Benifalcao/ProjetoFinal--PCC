from django.shortcuts import render, redirect
from .models import Troca
from .forms import TrocaForm


def index(request):
    return render(request, 'trocas/listar.html')


def listar_trocas(request):
    trocas = Troca.objects.all()

    return render(request, 'trocas/listar.html', {
        'trocas': trocas
    })


def criar_troca(request):
    if request.method == 'POST':
        form = TrocaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('listar_trocas')
    else:
        form = TrocaForm()

    return render(request, 'trocas/criar.html', {
        'form': form
    })