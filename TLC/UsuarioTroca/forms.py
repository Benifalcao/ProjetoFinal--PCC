from django import forms
from .models import UsuarioTroca


class UsuarioTrocaForm(forms.ModelForm):
    class Meta:
        model = UsuarioTroca
        fields = '__all__'


class UsuarioTrocaEdicaoForm(forms.ModelForm):
    class Meta:
        model = UsuarioTroca
        fields = [
            'troca',
            'status',
            'dataInicio',
            'protocolo',
            'DataRenovacao'
        ]
