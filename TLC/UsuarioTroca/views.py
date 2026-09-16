from django.shortcuts import render, redirect, get_object_or_404
from .models import UsuarioTroca
from .forms import UsuarioTrocaForm

def listar_usuario_troca(request):
    usuarios_troca = UsuarioTroca.objects.all()
    # ALTERAÇÃO: Caminho do template ajustado para o nome exato da pasta 'usuarioTroca'
    return render(request, 'usuarioTroca/listar_usuario_troca.html', {'usuarios_troca': usuarios_troca})

def criar_usuario_troca(request):
    if request.method == 'POST':
        form = UsuarioTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuariotroca:listar')
    else:
        form = UsuarioTrocaForm()
    # ALTERAÇÃO: Renderiza o form de criação dentro da pasta de templates correta
    return render(request, 'usuarioTroca/criar_usuario_troca.html', {'form': form})

def detalhar_usuario_troca(request, pk):
    item = get_object_or_404(UsuarioTroca, pk=pk)
    # ALTERAÇÃO: Aponta para o template detalhar.html
    return render(request, 'usuarioTroca/detalhar.html', {'item': item})

def editar_usuario_troca(request, pk):
    item = get_object_or_404(UsuarioTroca, pk=pk)
    if request.method == 'POST':
        form = UsuarioTrocaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('usuariotroca:listar')
    else:
        form = UsuarioTrocaForm(instance=item)
    # ALTERAÇÃO: Passa 'form' e 'item' para a edição
    return render(request, 'usuarioTroca/editar.html', {'form': form, 'item': item})

def deletar_usuario_troca(request, pk):
    # ALTERAÇÃO: Correção total de alinhamento/indentação e remoção da necessidade de template extra
    item = get_object_or_404(UsuarioTroca, pk=pk)
    item.delete()
    return redirect('usuariotroca:listar')