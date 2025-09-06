from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from authentification.models import CustomUser


class Billet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    image = models.ImageField(upload_to="articles", null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.user}, {self.time_created}"


class Commentaire(models.Model):
    RATING_CHOICES = [(i, f"{i}") for i in range(0, 6)]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    billet = models.ForeignKey(Billet, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, validators=[MinValueValidator(0), MaxValueValidator(5)], default=0
    )
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline}, {self.user}, {self.time_created} - Note: {self.rating}/5"
