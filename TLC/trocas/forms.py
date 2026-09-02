from django import forms
from .models import Troca, UsuarioTroca, ObjetoTroca

class TrocaForm(forms.ModelForm):
    class Meta:
        model = Troca
        fields = ['status', 'ofertantes', 'data_inicial', 'data_resposta', 'interessado']

class UsuarioTrocaForm(forms.ModelForm):
    class Meta:
        model = UsuarioTroca
        fields = ['usuario', 'troca', 'status', 'data_inicio', 'protocolo', 'data_renovacao']

class ObjetoTrocaForm(forms.ModelForm):
    class Meta:
        model = ObjetoTroca
        fields = ['objeto', 'troca', 'quant', 'data_troca', 'observacao']