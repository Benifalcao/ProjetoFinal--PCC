from django import forms
from .models import Troca


class TrocaForm(forms.ModelForm):
    class Meta:
        model = Troca
        fields = [
            'status',
            'ofertantes',
            'data_inicial',
            'data_resposta',
            'interessado'
        ]