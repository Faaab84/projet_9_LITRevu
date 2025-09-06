"""Module contenant les vues pour l'authentification et la gestion des relations de suivi.

Ce module définit les vues pour l'inscription, la connexion, la déconnexion,
ainsi que le suivi et l'arrêt du suivi des utilisateurs.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomAuthenticationForm, FollowUserForm


def register(request):
    """Gère l'inscription d'un nouvel utilisateur.

    Affiche un formulaire d'inscription et enregistre l'utilisateur si les données
    sont valides, puis redirige vers la page de connexion.
    """
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Compte créé pour {username} ! "
                "Vous pouvez maintenant vous connecter."
            )
            return redirect("authentification:login")
    else:
        form = CustomUserCreationForm()
    return render(request, "authentification/register.html", {"form": form})


def login_view(request):
    """Gère la connexion d'un utilisateur.

    Affiche un formulaire de connexion et authentifie l'utilisateur si les données
    sont valides, puis redirige vers le flux de l'application.
    """
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Bienvenue, {username} !")
                return redirect("reviews:feed")
            else:
                messages.error(
                    request,
                    "Nom d'utilisateur ou mot de passe incorrect."
                )
    else:
        form = CustomAuthenticationForm()
    return render(request, "authentification/login.html", {"form": form})


@login_required
def logout_view(request):
    """Gère la déconnexion d'un utilisateur.

    Déconnecte l'utilisateur et redirige vers la page de connexion.
    """
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect("authentification:login")


@login_required
def follow_user(request):
    """Permet à un utilisateur de suivre un autre utilisateur.

    Affiche un formulaire pour suivre un utilisateur et met à jour les relations
    de suivi si les données sont valides.
    """
    User = get_user_model()
    if request.method == "POST":
        form = FollowUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            try:
                user_to_follow = User.objects.get(username=username)
                if user_to_follow == request.user:
                    messages.error(
                        request,
                        "Vous ne pouvez pas vous suivre vous-même."
                    )
                elif user_to_follow in request.user.following.all():
                    messages.error(request, f"Vous suivez déjà {username}.")
                else:
                    request.user.following.add(user_to_follow)
                    messages.success(
                        request,
                        f"Vous suivez maintenant {username}."
                    )
            except User.DoesNotExist:
                messages.error(request, "Cet utilisateur n'existe pas.")
            return redirect("authentification:follow-user")
    else:
        form = FollowUserForm()

    following = request.user.following.all()
    followers = request.user.followers.all()
    return render(request, "authentification/follow_user.html", {
        "form": form,
        "following": following,
        "followers": followers
    })


@login_required
def unfollow_user(request, user_id):
    """Permet à un utilisateur d'arrêter de suivre un autre utilisateur.

    Supprime la relation de suivi pour l'utilisateur spécifié et redirige
    vers la page de suivi.
    """
    User = get_user_model()
    try:
        user_to_unfollow = User.objects.get(id=user_id)
        if user_to_unfollow in request.user.following.all():
            request.user.following.remove(user_to_unfollow)
            messages.success(
                request,
                f"Vous ne suivez plus {user_to_unfollow.username}."
            )
        else:
            messages.error(
                request,
                f"Vous ne suivez pas {user_to_unfollow.username}."
            )
    except User.DoesNotExist:
        messages.error(request, "Cet utilisateur n'existe pas.")
    return redirect("authentification:follow-user")
