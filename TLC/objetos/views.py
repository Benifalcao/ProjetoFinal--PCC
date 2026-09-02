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
            objeto = form.save(commit=False)
            objeto.usuario = request.user
            objeto.save()

            return redirect('listar_objetos')

    else:
        form = ObjetoForm()

    return render(request, 'objetos/criar.html', {
        'form': form
    })
# Create your views here.
