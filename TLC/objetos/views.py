from django.shortcuts import render, redirect, get_object_or_404
from usuario.models import Usuario
from django.shortcuts import render, redirect
from .models import Objeto
from .forms import ObjetoForm


def listar_objetos(request):
    objetos = Objeto.objects.all()

    return render(request, 'objetos/listar.html', {
        'objetos': objetos
    })


def criar_objeto(request):
    if request.method == 'POST':
        form = ObjetoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o objeto com o usuario selecionado no dropdown!
            return redirect('listar_objetos')  # Ajuste para a sua rota de listagem
    else:
        form = ObjetoForm()

    return render(request, 'objetos/criar.html', {'form': form})
# --Novasviews--

def detalhar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    return render(request, 'objetos/detalhar.html', {
        'objeto': objeto
    })

def editar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    if request.method == 'POST':
        form = ObjetoForm(request.POST, request.FILES, instance=objeto)
        if form.is_valid():
            form.save()
            return redirect('detalhar_objeto', pk=objeto.pk)
    else:
        form = ObjetoForm(instance=objeto)
    return render(request, 'objetos/editar.html', {
        'form': form,
        'objeto': objeto
    })

def deletar_objeto(request, pk):
    objeto = get_object_or_404(Objeto, pk=pk)
    if request.method == 'POST':
        objeto.delete()
        return redirect('listar_objetos')
    return render(request, 'objetos/deletar.html', {
        'objeto': objeto
    })