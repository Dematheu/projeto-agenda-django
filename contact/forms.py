from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'email',
            )

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 1.',
                code='invalid'
            )
        )
        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de erro 2.',
                code='invalid'
            )
        )

        return super().clean()
