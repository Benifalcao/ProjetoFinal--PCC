from django import forms
from .models import Usuario


class CadastroForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput, min_length=6)
    password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'nome', 'telefone']
        labels = {
            'username': 'Login',
            'nome': 'Nome completo',
            'telefone': 'Telefone',
        }
        help_texts = {'username': ''}

    def clean(self):
        dados = super().clean()
        senha = dados.get('password')
        confirmacao = dados.get('password2')
        if senha and confirmacao and senha != confirmacao:
            self.add_error('password2', 'As senhas não conferem.')
        return dados