from django import forms
from .models import ObjetoTroca


class ObjetoTrocaForm(forms.ModelForm):
    class Meta:
        model = ObjetoTroca
        fields = '__all__'


class ObjetoTrocaEdicaoForm(forms.ModelForm):
    class Meta:
        model = ObjetoTroca
        fields = [
            'quant',
            'data_troca',
            'obsevação'
        ]