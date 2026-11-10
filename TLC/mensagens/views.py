from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from trocas.models import Troca
from UsuarioTroca.models import UsuarioTroca
from .forms import MensagemForm


def _pode_participar(user, troca):
    if user.is_superuser:
        return True
    return UsuarioTroca.objects.filter(troca=troca, usuario_id=user.pk).exists()


@login_required
def minhas_conversas(request):
    if request.user.is_superuser:
        trocas = Troca.objects.all()
    else:
        ids = UsuarioTroca.objects.filter(usuario_id=request.user.pk).values_list('troca_id', flat=True)
        trocas = Troca.objects.filter(pk__in=ids)
    trocas = trocas.annotate(total_mensagens=Count('mensagens')).order_by('-id')
    return render(request, 'mensagens/minhas_conversas.html', {'trocas': trocas})


@login_required
def conversa(request, troca_id):
    troca = get_object_or_404(Troca, pk=troca_id)
    if not _pode_participar(request.user, troca):
        raise PermissionDenied

    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.troca = troca
            mensagem.remetente = request.user
            mensagem.save()
            return redirect('mensagens:conversa', troca_id=troca.pk)
    else:
        form = MensagemForm()

    mensagens = troca.mensagens.select_related('remetente')
    return render(request, 'mensagens/conversa.html', {
        'troca': troca,
        'mensagens': mensagens,
        'form': form,
    })