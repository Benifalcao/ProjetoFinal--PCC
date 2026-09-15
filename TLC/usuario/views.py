

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
            password = form.cleaned_data['password']

            # Verifica se já existe um User cadastrado com esse username
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Este nome de usuário já está em uso. Escolha outro.')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )
                usuario = form.save(commit=False)
                usuario.user = user
                usuario.save()
                return redirect('usuario_list')  # Se tiver namespace, use 'usuario:usuario_list'
    else:
        form = UsuarioForm()

    # Se o form for inválido ou o username já existir, re-renderiza a página mostrando os erros
    return render(request, 'usuario/usuario_form.html', {'form': form})