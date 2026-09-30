from django.shortcuts import render, redirect, get_object_or_404
from .models import ObjetoTroca
from .forms import ObjetoTrocaForm
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('objetotroca.add_objetotroca', raise_exception=True)
def listar_objeto_troca(request):
    objetos_troca = ObjetoTroca.objects.all()
    return render(request, 'ObjetoTroca/listar_objeto_troca.html', {'objetos_troca': objetos_troca})

@login_required
@permission_required('objetotroca.add_objetotroca', raise_exception=True)
def criar_objeto_troca(request):
    if request.method == 'POST':
        form = ObjetoTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objetotroca:listar')
    else:
        form = ObjetoTrocaForm()
    return render(request, 'ObjetoTroca/criar_objeto_troca.html', {'form': form})

@login_required
@permission_required('objetotroca.add_objetotroca', raise_exception=True)
def detalhar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)
    return render(request, 'ObjetoTroca/detalhar.html', {'item': item})

@login_required
@permission_required('objetotroca.change_objetotroca', raise_exception=True)
def editar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)
    if request.method == 'POST':
        form = ObjetoTrocaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('objetotroca:listar')
    else:
        form = ObjetoTrocaForm(instance=item)
    return render(request, 'ObjetoTroca/editar.html', {'form': form, 'item': item})

@login_required
@permission_required('objetotroca.delete_objetotroca', raise_exception=True)
def deletar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)
    item.delete()
    return redirect('objetotroca:listar')