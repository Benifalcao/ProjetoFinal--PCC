from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('usuario:usuario_list')
        else:
            return render(request, 'registration/login.html', {'erro': 'Usuário ou senha inválidos'})
    return render(request, 'registration/login.html')


def logout_view(request):
    auth_logout(request)
    return redirect('login')