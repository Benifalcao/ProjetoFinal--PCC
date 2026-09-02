from django.shortcuts import render, redirect
from .models import Troca, UsuarioTroca, ObjetoTroca
from .forms import TrocaForm, UsuarioTrocaForm, ObjetoTrocaForm

# Views de Troca
def index(request):
    return render(request, 'trocas/listar.html')

def listar_trocas(request):
    trocas = Troca.objects.all()
    return render(request, 'trocas/listar.html', {'trocas': trocas})

def criar_troca(request):
    if request.method == 'POST':
        form = TrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_trocas')
    else:
        form = TrocaForm()
    return render(request, 'trocas/criar.html', {'form': form})

# Views de ObjetoTroca
def criar_objeto_troca(request):
    if request.method == 'POST':
        form = ObjetoTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_trocas')
    else:
        form = ObjetoTrocaForm()
    return render(request, 'trocas/criar_objeto_troca.html', {'form': form})
    

def listar_usuarios_troca(request):
    usuarios_troca = UsuarioTroca.objects.all()
    return render(request, 'trocas/listar_usuario_troca.html', {'usuarios_troca': usuarios_troca})

def criar_usuario_troca(request):
    if request.method == 'POST':
        form = UsuarioTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios_troca')
    else:
        form = UsuarioTrocaForm()
    return render(request, 'trocas/criar_usuario_troca.html', {'form': form})