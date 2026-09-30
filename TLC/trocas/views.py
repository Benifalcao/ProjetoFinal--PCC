
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Troca
from .forms import TrocaForm
from django.contrib.auth.decorators import login_required, permission_required


def index(request):
    return render(request, 'trocas/listar.html')

@login_required
def listar_trocas(request):
    trocas = Troca.objects.all()
    return render(request, 'trocas/listar.html', {'trocas': trocas})

# CRIAR
@login_required
@permission_required('trocas.add_trocas', raise_exception=True)
def criar_troca(request):
    if request.method == 'POST':
        form = TrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trocas:listar_trocas')
    else:
        form = TrocaForm()
    return render(request, 'trocas/criar.html', {'form': form})

#DETALHAR
@login_required
def detalhar_troca(request, pk):
    troca = get_object_or_404(Troca, pk=pk)
    return render(request, 'trocas/detalhar.html', {'troca': troca})

# EDITAR
@login_required
@permission_required('trocas.change_trocas', raise_exception=True)
def editar_troca(request, pk):
    troca = get_object_or_404(Troca, pk=pk)
    if request.method == 'POST':
        form = TrocaForm(request.POST, instance=troca)
        if form.is_valid():
            form.save()
            return redirect('trocas:listar_trocas')
    else:
        form = TrocaForm(instance=troca)
    return render(request, 'trocas/editar.html', {'form': form, 'troca': troca})
   
@login_required
@permission_required('trocas.delete_trocas', raise_exception=True)
def deletar_troca(request, pk):
    troca = get_object_or_404(Troca, pk=pk)
    troca.delete()
    return redirect('trocas:listar_trocas')