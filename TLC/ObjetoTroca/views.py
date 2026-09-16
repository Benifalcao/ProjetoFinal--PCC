from django.shortcuts import render, redirect, get_object_or_404
from .models import ObjetoTroca
from .forms import ObjetoTrocaForm

def listar_objeto_troca(request):
    objetos_troca = ObjetoTroca.objects.all()
    # ALTERAÇÃO: Correção do nome da função e apontamento de template correto
    return render(request, 'ObjetoTroca/listar_objeto_troca.html', {'objetos_troca': objetos_troca})

def criar_objeto_troca(request):
    if request.method == 'POST':
        form = ObjetoTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('objetotroca:listar')
    else:
        form = ObjetoTrocaForm()
    # ALTERAÇÃO: Renderiza o form de criação dentro de ObjetoTroca
    return render(request, 'ObjetoTroca/criar_objeto_troca.html', {'form': form})

def detalhar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)
    # ALTERAÇÃO: Aponta para o detalhar.html do ObjetoTroca
    return render(request, 'ObjetoTroca/detalhar.html', {'item': item})

def editar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)
    if request.method == 'POST':
        form = ObjetoTrocaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('objetotroca:listar')
    else:
        form = ObjetoTrocaForm(instance=item)
    # ALTERAÇÃO: Passa 'form' e 'item' para a edição
    return render(request, 'ObjetoTroca/editar.html', {'form': form, 'item': item})

def deletar_objeto_troca(request, pk):
    # ALTERAÇÃO: Deleção direta com redirecionamento limpo
    item = get_object_or_404(ObjetoTroca, pk=pk)
    item.delete()
    return redirect('objetotroca:listar')