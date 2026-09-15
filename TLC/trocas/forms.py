from django import forms
from .models import Troca

class TrocaForm(forms.ModelForm):
    class Meta:
        model = Troca
        fields = ['status', 'ofertantes', 'data_inicial', 'data_resposta', 'interessado', 'usuarios']
        widgets = {
            'data_inicial': forms.DateInput(attrs={'type': 'date'}),
            'data_resposta': forms.DateInput(attrs={'type': 'date'}),
        }

        from django import forms
from .models import Troca
