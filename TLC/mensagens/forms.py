from django import forms
from .models import Mensagem


class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Escreva sua mensagem...',
            }),
        }
        labels = {'texto': 'Mensagem'}