from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import UsuarioTroca
from .forms import UsuarioTrocaForm

APP = UsuarioTroca._meta.app_label


@login_required
@permission_required(f'{APP}.view_usuariotroca', raise_exception=True)
def listar_usuario_troca(request):
    usuarios_troca = UsuarioTroca.objects.all()
    return render(request, 'usuarioTroca/listar_usuario_troca.html', {'usuarios_troca': usuarios_troca})


@login_required
@permission_required(f'{APP}.add_usuariotroca', raise_exception=True)
def criar_usuario_troca(request):
    if request.method == 'POST':
        form = UsuarioTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vínculo criado com sucesso.')
            return redirect('usuariotroca:listar')
    else:
        form = UsuarioTrocaForm()
    return render(request, 'usuarioTroca/criar_usuario_troca.html', {'form': form})


@login_required
@permission_required(f'{APP}.view_usuariotroca', raise_exception=True)
def detalhar_usuario_troca(request, pk):
    item = get_object_or_404(UsuarioTroca, pk=pk)
    return render(request, 'usuarioTroca/detalhar.html', {'item': item})


@login_required
@permission_required(f'{APP}.change_usuariotroca', raise_exception=True)
def editar_usuario_troca(request, pk):
    item = get_object_or_404(UsuarioTroca, pk=pk)
    if request.method == 'POST':
        form = UsuarioTrocaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vínculo atualizado com sucesso.')
            return redirect('usuariotroca:listar')
    else:
        form = UsuarioTrocaForm(instance=item)
    return render(request, 'usuarioTroca/editar.html', {'form': form, 'item': item})


@login_required
@permission_required(f'{APP}.delete_usuariotroca', raise_exception=True)
def deletar_usuario_troca(request, pk):
    item = get_object_or_404(UsuarioTroca, pk=pk)
    item.delete()
    messages.success(request, 'Vínculo deletado com sucesso.')
    return redirect('usuariotroca:listar')