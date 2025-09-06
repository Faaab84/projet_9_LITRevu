from django import forms
from .models import Billet, Commentaire


class RequestBilletForm(forms.ModelForm):
    """Formulaire pour la création ou la modification d'un billet."""

    class Meta:
        model = Billet
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class RequestCommentaireForm(forms.ModelForm):
    """Formulaire pour la création ou la modification d'un commentaire."""

    RATING_CHOICES = [(i, str(i)) for i in range(6)]
    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Note'
    )

    class Meta:
        model = Commentaire
        fields = ['headline', 'rating', 'body']
        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'headline': 'Titre :',
            'body': 'Commentaire :',
        }
