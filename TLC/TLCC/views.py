from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme

from usuario.permissoes import obter_grupo_comum


def login_view(request):
    if request.user.is_authenticated:
        return redirect('bem_vindo')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_superuser:
                user.groups.add(obter_grupo_comum())
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.get_username()}!')
            proximo = request.POST.get('next') or request.GET.get('next')
            if proximo and url_has_allowed_host_and_scheme(proximo, allowed_hosts={request.get_host()}):
                return redirect(proximo)
            return redirect('bem_vindo')
    else:
        form = AuthenticationForm(request)

    return render(request, 'login.html', {'form': form, 'next': request.GET.get('next', '')})


def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('login')