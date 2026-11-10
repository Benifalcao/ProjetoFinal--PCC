from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

from .models import Usuario
from .forms import UsuarioForm
from .forms_cadastro import CadastroForm
from .permissoes import obter_grupo_comum


def _pode_gerenciar(request, usuario):
    """Só o admin master ou o próprio dono da conta."""
    return request.user.is_superuser or request.user.pk == usuario.pk


def usuario_cadastro(request):
    if request.user.is_authenticated:
        return redirect('bem_vindo')

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.is_staff = False
            usuario.is_superuser = False
            usuario.save()
            usuario.groups.add(obter_grupo_comum())
            messages.success(request, 'Conta criada com sucesso! Faça login para entrar.')
            return redirect('login')
    else:
        form = CadastroForm()

    return render(request, 'usuario/cadastro.html', {'form': form})


@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuario/usuario_list.html", {"usuarios": usuarios})


@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def usuario_detail(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    return render(request, "usuario/usuario_detail.html", {"usuario": usuario})


@login_required
@permission_required('usuario.add_usuario', raise_exception=True)
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Este nome de usuário já está em uso. Escolha outro.')
            else:
                usuario = form.save(commit=False)
                usuario.set_password(form.cleaned_data['password'])
                usuario.save()
                usuario.groups.add(obter_grupo_comum())
                messages.success(request, 'Usuário cadastrado com sucesso.')
                return redirect('usuario:usuario_list')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/usuario_form.html', {'form': form})


@login_required
def usuario_editar(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if not _pode_gerenciar(request, usuario):
        raise PermissionDenied

    era_superuser = usuario.is_superuser
    era_staff = usuario.is_staff

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exclude(pk=usuario.pk).exists():
                form.add_error('username', 'Este nome de usuário já está em uso. Escolha outro.')
            else:
                usuario_editado = form.save(commit=False)
                if not request.user.is_superuser:
                    usuario_editado.is_superuser = era_superuser
                    usuario_editado.is_staff = era_staff
                nova_senha = form.cleaned_data.get('password')
                if nova_senha:
                    usuario_editado.set_password(nova_senha)
                usuario_editado.save()
                if nova_senha and request.user.pk == usuario_editado.pk:
                    update_session_auth_hash(request, usuario_editado)
                messages.success(request, 'Dados atualizados com sucesso.')
                return redirect('usuario:usuario_detail', usuario_id=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario, initial={'password': ''})

    return render(request, 'usuario/usuario_editar.html', {'form': form, 'usuario': usuario})


@login_required
def usuario_excluir(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if not _pode_gerenciar(request, usuario):
        raise PermissionDenied

    if usuario.is_superuser:
        messages.error(request, 'A conta do administrador master não pode ser excluída por aqui.')
        return redirect('usuario:usuario_detail', usuario_id=usuario.pk)

    if request.method == 'POST':
        propria_conta = request.user.pk == usuario.pk
        usuario.delete()
        if propria_conta:
            logout(request)
            messages.info(request, 'Sua conta foi excluída.')
            return redirect('login')
        messages.success(request, 'Usuário excluído com sucesso.')
        return redirect('usuario:usuario_list')

    return render(request, 'usuario/usuario_excluir.html', {'usuario': usuario})