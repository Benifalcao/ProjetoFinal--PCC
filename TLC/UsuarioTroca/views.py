
# Create your views here.
from django.shortcuts import render, redirect
from .models import UsuarioTroca
from .forms import UsuarioTrocaForm


def listar_usuarios_troca(request):
    usuarios_troca = UsuarioTroca.objects.all()
    return render(request, 'UsuarioTroca/listar_usuario_troca.html', {'usuarios_troca': usuarios_troca})


def criar_usuario_troca(request):
    if request.method == 'POST':
        form = UsuarioTrocaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('UsuarioTroca:listar_usuarios_troca')
    else:
        form = UsuarioTrocaForm()
    return render(request, 'UsuarioTroca/criar_usuario_troca.html', {'form': form})