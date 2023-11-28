from django import forms
from reservas.models import Hospedes

class FormHosEditar(forms.ModelForm):
    class Meta:
        model = Hospedes
        fields = ['nome','email', 'data_nasci', 'cpf', 'telefone', 'cidade', 'estado' ] 