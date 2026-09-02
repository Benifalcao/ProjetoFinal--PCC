from django import forms
from .models import Objeto


class ObjetoForm(forms.ModelForm):
    class Meta:
        model = Objeto
        fields = ['nome', 'descricao', 'valor_avaliacao', 'status']
        