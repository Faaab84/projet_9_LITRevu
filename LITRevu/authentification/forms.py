# authentification/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nom d’utilisateur',
            'email': 'Adresse e-mail',
            'password1': 'Mot de passe',
            'password2': 'Confirmation du mot de passe',
        }
        help_texts = {
            'username': 'Requis. 150 caractères ou moins. Lettres, chiffres et @/./+/-/_ uniquement.',
            'email': '',
            'password1': 'Votre mot de passe doit contenir au moins 8 caractères, ne pas être trop similaire à vos autres informations personnelles, ne pas être un mot de passe couramment utilisé, et ne peut pas être entièrement numérique.',
            'password2': 'Entrez le même mot de passe que précédemment, pour vérification.',
        }

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
        self.fields['username'].label = 'Nom d’utilisateur'
        self.fields['password'].label = 'Mot de passe'


class FollowUserForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Nom d’utilisateur à suivre',
        widget=forms.TextInput(attrs={'class': 'form-control', 'aria-label': 'Nom d’utilisateur à suivre'})
    )
