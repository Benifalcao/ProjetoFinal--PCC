from django.shortcuts import render, redirect, get_object_or_404
from .models import Troca
from .forms import TrocaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from UsuarioTroca.models import UsuarioTroca
from usuario.models import Usuario
from django.utils import timezone
import uuid


# Responde se o usuário logado pode alterar (editar/excluir) esta troca
def usuario_pode_alterar(request, troca):
    return request.user.is_superuser or troca.usuarios.filter(pk=request.user.pk).exists()


@login_required
def index(request):
    return redirect('trocas:listar_trocas')


@login_required
@permission_required('trocas.view_troca', raise_exception=True)
def listar_trocas(request):
    trocas = list(Troca.objects.all())

    # Consulta as trocas das quais o usuário participa
    minhas = set(
        Troca.objects.filter(usuarios__pk=request.user.pk).values_list('pk', flat=True)
    )

    for troca in trocas:
        troca.pode_alterar = request.user.is_superuser or troca.pk in minhas

    return render(request, 'trocas/listar.html', {'trocas': trocas})


# CRIAR
@login_required
@permission_required('trocas.add_troca', raise_exception=True)
def criar_troca(request):
    if request.method == 'POST':
        form = TrocaForm(request.POST)

        if form.is_valid():
            troca = form.save()

            # Procura o registro do usuário na tabela Usuario
            usuario = Usuario.objects.filter(pk=request.user.pk).first()

            # Se encontrar, registra automaticamente sua participação
            if usuario:
                UsuarioTroca.objects.get_or_create(
                    usuario=usuario,
                    troca=troca,
                    defaults={
                        'status': 'Participante',
                        'dataInicio': timezone.now().strftime('%Y-%m-%d'),
                        'protocolo': str(uuid.uuid4()),
                    }
                )

            messages.success(request, 'Troca cadastrada com sucesso!')
            return redirect('trocas:listar_trocas')
    else:
        form = TrocaForm()

    return render(request, 'trocas/criar.html', {'form': form})


# DETALHAR
@login_required
@permission_required('trocas.view_troca', raise_exception=True)
def detalhar_troca(request, pk):
    troca = get_object_or_404(Troca, pk=pk)

    return render(request, 'trocas/detalhar.html', {
        'troca': troca,
        'pode_alterar': usuario_pode_alterar(request, troca),
    })


# EDITAR
@login_required
@permission_required('trocas.change_troca', raise_exception=True)
def editar_troca(request, pk):
    troca = get_object_or_404(Troca, pk=pk)

    if not usuario_pode_alterar(request, troca):
        messages.error(request, 'Você só pode editar trocas em que participa.')
        return redirect('trocas:listar_trocas')

    if request.method == 'POST':
        form = TrocaForm(request.POST, instance=troca)

        if form.is_valid():
            form.save()
            messages.success(request, 'Troca editada com sucesso!')
            return redirect('trocas:listar_trocas')
    else:
        form = TrocaForm(instance=troca)

    return render(request, 'trocas/editar.html', {'form': form, 'troca': troca})


# DELETAR
@login_required
@permission_required('trocas.delete_troca', raise_exception=True)
def deletar_troca(request, pk):
    troca = get_object_or_404(Troca, pk=pk)

    if not usuario_pode_alterar(request, troca):
        messages.error(request, 'Você só pode excluir trocas em que participa.')
        return redirect('trocas:listar_trocas')

    troca.delete()
    messages.success(request, 'Troca excluída com sucesso!')
    return redirect('trocas:listar_trocas')
