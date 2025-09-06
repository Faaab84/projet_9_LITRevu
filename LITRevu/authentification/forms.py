"""Module contenant les formulaires personnalisés pour l'authentification et la gestion des utilisateurs."""

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Formulaire pour la création d'un nouvel utilisateur personnalisé.

    Ce formulaire étend UserCreationForm pour inclure des champs personnalisés
    et des attributs de style pour l'interface utilisateur.
    """

    class Meta:
        """Configuration des métadonnées pour le formulaire de création d'utilisateur."""
        model = CustomUser
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Nom d’utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmation du mot de passe',
        }
        help_texts = {
            'username': (
                'Requis. 150 caractères ou moins. '
                'Lettres, chiffres et @/./+/-/_ uniquement.'
            ),
            'password1': (
                'Votre mot de passe doit contenir au moins 8 caractères, '
                'ne pas être trop similaire à vos autres informations personnelles, '
                'ne pas être un mot de passe couramment utilisé, '
                'et ne peut pas être entièrement numérique.'
            ),
            'password2': (
                'Entrez le même mot de passe que précédemment, '
                'pour vérification.'
            ),
        }

    def __init__(self, *args, **kwargs):
        """Initialise le formulaire avec des attributs de style pour les champs."""
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'aria-label': 'Nom d’utilisateur',
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
    """Formulaire pour l'authentification d'un utilisateur existant.

    Ce formulaire étend AuthenticationForm pour personnaliser les champs
    et ajouter des attributs de style.
    """

    def __init__(self, *args, **kwargs):
        """Initialise le formulaire avec des attributs de style pour les champs."""
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
    """Formulaire pour permettre à un utilisateur de suivre un autre utilisateur."""
    username = forms.CharField(
        max_length=150,
        label='Nom d’utilisateur à suivre',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'aria-label': 'Nom d’utilisateur à suivre'
        })
    )
