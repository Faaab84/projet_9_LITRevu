"""Module définissant les URL pour l'application d'authentification.

Ce module configure les chemins d'URL pour l'inscription, la connexion,
la déconnexion, et la gestion des relations de suivi entre utilisateurs.
"""

from django.urls import path
from . import views

app_name = 'authentification'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('follow/', views.follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow-user'),
]
