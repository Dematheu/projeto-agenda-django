from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Seu nome',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para o usuário.'
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Seu nome - init',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'email',
            'phone', 'description', 'category',
            )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Seu nome',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                    'Primeiro nome não pode ser igual o segundo',
                    code='invalid'
                )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Error add_error',
                    code='invalid'
                )
            )

        return first_name