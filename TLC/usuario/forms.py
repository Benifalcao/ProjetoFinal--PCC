
from django import forms
from django.contrib.auth.models import User
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'nome', 'telefone', 'password']

