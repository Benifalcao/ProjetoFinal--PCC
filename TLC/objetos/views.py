from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from usuario.models import Usuario
from .models import Objeto
from .forms import ObjetoForm


def usuario_pode_alterar(request, objeto):
    return (
        request.user.is_superuser
        or objeto.usuario_id == request.user.pk
    )


@login_required
@permission_required('objetos.view_objeto', raise_exception=True)
def listar_objetos(request):
    objetos = Objeto.objects.all()

    for objeto in objetos:
        objeto.pode_alterar = usuario_pode_alterar(request, objeto)

    return render(request, 'objetos/listar.html', {
        'objetos': objetos
    })


@login_required
@permission_required('objetos.add_objeto', raise_exception=True)
def criar_objeto(request):
    if request.method == 'POST':
        form = ObjetoForm(request.POST, request.FILES)

        if form.is_valid():
            usuario = Usuario.objects.filter(pk=request.user.pk).first()

            if usuario is None:
                messages.error(
                    request,
                    'Não foi possível identificar seu cadastro de usuário.'
                )
                return redirect('listar_objetos')

            objeto = form.save(commit=False)
            objeto.usuario = usuario
            objeto.save()

            messages.success(request, 'Objeto cadastrado com sucesso!')
            return redirect('listar_objetos')

    else:
        form = ObjetoForm()

    return render(request, 'objetos/criar.html', {
        'form': form
    })


@login_required
@permission_required('objetos.view_objeto', raise_exception=True)
def detalhar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)

    return render(request, 'objetos/detalhar.html', {
        'objeto': objeto,
        'pode_alterar': usuario_pode_alterar(request, objeto)
    })


@login_required
@permission_required('objetos.change_objeto', raise_exception=True)
def editar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)

    if not usuario_pode_alterar(request, objeto):
        messages.error(
            request,
            'Você só pode editar objetos que cadastrou.'
        )
        return redirect('listar_objetos')

    if request.method == 'POST':
        form = ObjetoForm(request.POST, request.FILES, instance=objeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Objeto editado com sucesso!')
            return redirect('detalhar_objeto', pk=objeto.pk)

    else:
        form = ObjetoForm(instance=objeto)

    return render(request, 'objetos/editar.html', {
        'form': form,
        'objeto': objeto
    })


@login_required
@permission_required('objetos.delete_objeto', raise_exception=True)
def deletar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)

    if not usuario_pode_alterar(request, objeto):
        messages.error(
            request,
            'Você só pode excluir objetos que cadastrou.'
        )
        return redirect('listar_objetos')

    if request.method == 'POST':
        objeto.delete()
        messages.success(request, 'Objeto excluído com sucesso!')
        return redirect('listar_objetos')

    return render(request, 'objetos/deletar.html', {
        'objeto': objeto
    })
