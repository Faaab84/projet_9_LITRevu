from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'aria-label': 'Nom d’utilisateur',
            'required': 'required'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'aria-label': 'Adresse e-mail',
            'required': 'required'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'aria-label': 'Mot de passe',
            'required': 'required'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'aria-label': 'Confirmation du mot de passe',
            'required': 'required'
        })


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'aria-label': 'Nom d’utilisateur',
            'required': 'required'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'aria-label': 'Mot de passe',
            'required': 'required'
        })

