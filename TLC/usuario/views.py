

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Usuario
from .forms import UsuarioForm


def usuario_list(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "usuario/usuario_list.html", context)


def usuario_detail(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    return render(request, "usuario/usuario_detail.html", {"usuario": usuario})



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
                return redirect('usuario:usuario_list')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/usuario_form.html', {'form': form})


def usuario_editar(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exclude(pk=usuario.pk).exists():
                form.add_error('username', 'Este nome de usuário já está em uso. Escolha outro.')
            else:
                usuario_editado = form.save(commit=False)
                nova_senha = form.cleaned_data.get('password')
                if nova_senha:
                    usuario_editado.set_password(nova_senha)
                usuario_editado.save()
                return redirect('usuario:usuario_detail', usuario_id=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario, initial={'password': ''})
    return render(request, 'usuario/usuario_editar.html', {'form': form, 'usuario': usuario})


def usuario_excluir(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario:usuario_list')
    return render(request, 'usuario/usuario_excluir.html', {'usuario': usuario})