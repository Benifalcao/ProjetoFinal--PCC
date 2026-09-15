
from django import forms
from .models import UsuarioTroca


class UsuarioTrocaForm(forms.ModelForm):
    class Meta:
        model = UsuarioTroca
        fields = ['usuario', 'troca', 'status', 'dataInicio', 'protocolo', 'DataRenovacao']