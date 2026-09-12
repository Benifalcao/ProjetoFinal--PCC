
from django import forms
from .models import ObjetoTroca


class ObjetoTrocaForm(forms.ModelForm):
    class Meta:
        model = ObjetoTroca
        fields = ['objeto', 'troca', 'quant', 'data_troca', 'obsevação']