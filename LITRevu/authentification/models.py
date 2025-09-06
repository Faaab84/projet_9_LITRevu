"""Module définissant le modèle d'utilisateur personnalisé pour l'application."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Modèle d'utilisateur personnalisé étendant AbstractUser.

    Ajoute des champs pour la biographie et les relations de suivi entre utilisateurs.
    """
    bio = models.TextField(max_length=500, blank=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        """Retourne une représentation sous forme de chaîne du nom d'utilisateur."""
        return self.username
