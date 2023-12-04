from typing import Any
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    perfil = forms.ChoiceField(
        choices=[
            ("atendente", 'Atendente'),
            ("gerente", "Gerente"),
        ],
    )
    # imagem = forms.ImageField(required=False)
    # telefone = forms.CharField(max_length=9, required=False)

    class Meta: #Uma classe interna que fornece metadados ao formulário. 
        # Especifica quais campos do modelo User devem ser incluídos no formulário
        model = User
        fields = ['first_name', 'last_name', 'email',
                    'username', 'password1', 'password2']
        
    def clean(self):

        email = self.cleaned_data.get('email')
        # telefone = self.cleaned_data.get('telefone')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                'E-mail ja existe!'
            )

        # if len(telefone) < 9:
        #     self.add_error(
        #         'telefone',
        #         'telefone inválido!'
        #     )
        return super().clean()


class UserEditForm(UserCreationForm):
    perfil = forms.ChoiceField(
        choices=[
            ("atendente", 'Atendente'),
            ("gerente", "Gerente"),
        ],
    )
    last_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )
    imagem = forms.ImageField(required=False)
    telefone = forms.CharField(max_length=9, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',
                  'password1', 'password2']