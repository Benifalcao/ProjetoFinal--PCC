from django import forms
from .models import ObjetoTroca

class ObjetoTrocaForm(forms.ModelForm):
    class Meta:
        model = ObjetoTroca
        fields = '__all__'  # Garante a leitura exata dos campos do model de ObjetoTroca