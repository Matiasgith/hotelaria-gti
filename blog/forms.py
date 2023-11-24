from django import forms

from .models import Comentario
# from django.utils import timezone

class ComentarioForm(forms.ModelForm):
    # class meta fala sobre a class de cima
    class Meta:
        model = Comentario
        fields = '__all__'
        widgets = {
            'texto': forms.Textarea(
                attrs={'placeholder': 'Digite seu ...'}
        ),
            'data': forms.DateInput(attrs={'type': 'date'}),
         
        }