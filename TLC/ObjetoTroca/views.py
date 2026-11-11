from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden

from .models import ObjetoTroca
from .forms import ObjetoTrocaForm, ObjetoTrocaEdicaoForm
from UsuarioTroca.models import UsuarioTroca

APP = ObjetoTroca._meta.app_label


def usuario_pode_alterar(request, item):
    return (
        request.user.is_superuser
        or item.objeto.usuario_id == request.user.pk
        or UsuarioTroca.objects.filter(
            usuario_id=request.user.pk,
            troca_id=item.troca_id
        ).exists()
    )


@login_required
@permission_required(f'{APP}.view_objetotroca', raise_exception=True)
def listar_objeto_troca(request):
    objetos_troca = ObjetoTroca.objects.all()

    for item in objetos_troca:
        item.pode_editar = (
            request.user.has_perm(f'{APP}.change_objetotroca')
            and usuario_pode_alterar(request, item)
        )

        item.pode_deletar = (
            request.user.has_perm(f'{APP}.delete_objetotroca')
            and usuario_pode_alterar(request, item)
        )

    return render(
        request,
        'ObjetoTroca/listar_objeto_troca.html',
        {'objetos_troca': objetos_troca}
    )


@login_required
@permission_required(f'{APP}.add_objetotroca', raise_exception=True)
def criar_objeto_troca(request):
    if request.method == 'POST':
        form = ObjetoTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Objeto adicionado à troca com sucesso.')
            return redirect('objetotroca:listar')
    else:
        form = ObjetoTrocaForm()

    return render(
        request,
        'ObjetoTroca/criar_objeto_troca.html',
        {'form': form}
    )


@login_required
@permission_required(f'{APP}.view_objetotroca', raise_exception=True)
def detalhar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)

    pode_editar = (
        request.user.has_perm(f'{APP}.change_objetotroca')
        and usuario_pode_alterar(request, item)
    )

    pode_deletar = (
        request.user.has_perm(f'{APP}.delete_objetotroca')
        and usuario_pode_alterar(request, item)
    )

    return render(
        request,
        'ObjetoTroca/detalhar.html',
        {
            'item': item,
            'pode_editar': pode_editar,
            'pode_deletar': pode_deletar
        }
    )


@login_required
@permission_required(f'{APP}.change_objetotroca', raise_exception=True)
def editar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)

    if not usuario_pode_alterar(request, item):
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = ObjetoTrocaEdicaoForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro atualizado com sucesso.')
            return redirect('objetotroca:listar')
    else:
        form = ObjetoTrocaEdicaoForm(instance=item)

    return render(
        request,
        'ObjetoTroca/editar.html',
        {'form': form, 'item': item}
    )


@login_required
@permission_required(f'{APP}.delete_objetotroca', raise_exception=True)
def deletar_objeto_troca(request, pk):
    item = get_object_or_404(ObjetoTroca, pk=pk)

    if not usuario_pode_alterar(request, item):
        return HttpResponseForbidden()

    item.delete()
    messages.success(request, 'Registro deletado com sucesso.')
    return redirect('objetotroca:listar')
