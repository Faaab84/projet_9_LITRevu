from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RequestBilletForm, RequestCommentaireForm
from .models import Billet, Commentaire
from django.contrib.auth import get_user_model
from itertools import chain
from django.db.models import CharField, Value, Q

@login_required
def feed(request):
    User = get_user_model()
    followed_users = request.user.following.all()
    billets = Billet.objects.filter(user__in=followed_users) | Billet.objects.filter(user=request.user)
    commentaires = Commentaire.objects.filter(user__in=followed_users) | Commentaire.objects.filter(user=request.user) | Commentaire.objects.filter(billet__user=request.user)
    billets = billets.annotate(content_type=Value('BILLET', CharField()))
    commentaires = commentaires.annotate(content_type=Value('COMMENTAIRE', CharField()))
    for billet in billets:
        billet.has_commentaire = billet.commentaire_set.filter(user=request.user).exists()
    posts = sorted(chain(billets, commentaires), key=lambda post: post.time_created, reverse=True)
    return render(request, "reviews/feed.html", {"posts": posts, "is_feed": True})

@login_required
def posts(request):
    billets = Billet.objects.filter(user=request.user)
    commentaires = Commentaire.objects.filter(user=request.user)
    billets = billets.annotate(content_type=Value('BILLET', CharField()))
    commentaires = commentaires.annotate(content_type=Value('COMMENTAIRE', CharField()))
    for billet in billets:
        billet.has_commentaire = billet.commentaire_set.filter(user=request.user).exists()
    user_posts = sorted(chain(billets, commentaires), key=lambda post: post.time_created, reverse=True)
    return render(request, "reviews/posts.html", {"posts": user_posts, "is_feed": False})

@login_required
def show_billet_form(request):
    form = RequestBilletForm()
    return render(request, "reviews/show_billet_form.html", {"form": form})

@login_required
def create_billet(request):
    if request.method == "POST":
        form = RequestBilletForm(request.POST, request.FILES)
        if form.is_valid():
            billet = form.save(commit=False)
            billet.user = request.user
            billet.save()
            messages.success(request, f"Billet '{billet.title}' créé avec succès.")
            return redirect("reviews:feed")
        else:
            messages.error(request, "Erreur dans le formulaire. Vérifiez les champs.")
    else:
        form = RequestBilletForm()
    return render(request, "reviews/show_billet_form.html", {"form": form})

@login_required
def edit_billet(request, billet_id):
    billet = get_object_or_404(Billet, id=billet_id, user=request.user)
    if request.method == "POST":
        form = RequestBilletForm(request.POST, request.FILES, instance=billet)
        if form.is_valid():
            form.save()
            messages.success(request, "Billet modifié avec succès.")
            return redirect("reviews:feed")
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = RequestBilletForm(instance=billet)
    return render(request, "reviews/edit_billet.html", {"form": form, "billet": billet})

@login_required
def delete_billet(request, billet_id):
    billet = get_object_or_404(Billet, id=billet_id, user=request.user)
    if request.method == "POST":
        billet.delete()
        messages.success(request, "Billet supprimé avec succès.")
        return redirect("reviews:feed")
    return render(request, "reviews/delete_billet.html", {"billet": billet})

@login_required
def create_commentaire(request, billet_id=None):
    if billet_id:
        # Autoriser l'accès si le billet appartient à l'utilisateur ou à un suivi
        billet = get_object_or_404(Billet, Q(id=billet_id) & (Q(user__in=request.user.following.all()) | Q(user=request.user)))
    else:
        billet = None
    if request.method == "POST":
        form = RequestCommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.user = request.user
            commentaire.billet = billet
            commentaire.save()
            messages.success(request, "Critique créée avec succès.")
            return redirect("reviews:feed")
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = RequestCommentaireForm()
    return render(request, "reviews/create_commentaire.html", {"form": form, "billet": billet})

@login_required
def edit_commentaire(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, id=commentaire_id, user=request.user)
    if request.method == "POST":
        form = RequestCommentaireForm(request.POST, instance=commentaire)
        if form.is_valid():
            form.save()
            messages.success(request, "Critique modifiée avec succès.")
            return redirect("reviews:feed")
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = RequestCommentaireForm(instance=commentaire)
    return render(request, "reviews/edit_commentaire.html", {"form": form, "commentaire": commentaire})

@login_required
def delete_commentaire(request, commentaire_id):
    commentaire = get_object_or_404(Commentaire, id=commentaire_id, user=request.user)
    if request.method == "POST":
        commentaire.delete()
        messages.success(request, "Critique supprimée avec succès.")
        return redirect("reviews:feed")
    return render(request, "reviews/delete_commentaire.html", {"commentaire": commentaire})

@login_required
def create_billet_and_commentaire(request):
    billet_form = RequestBilletForm()
    commentaire_form = RequestCommentaireForm()
    if request.method == "POST":
        billet_form = RequestBilletForm(request.POST, request.FILES)
        commentaire_form = RequestCommentaireForm(request.POST)
        if billet_form.is_valid() and commentaire_form.is_valid():
            billet = billet_form.save(commit=False)
            billet.user = request.user
            billet.save()
            commentaire = commentaire_form.save(commit=False)
            commentaire.user = request.user
            commentaire.billet = billet
            commentaire.save()
            messages.success(request, "Billet et critique créés avec succès.")
            return redirect("reviews:feed")
        else:
            messages.error(request, "Erreur dans le formulaire.")
    return render(request, "reviews/create_billet_and_commentaire.html", {
        "billet_form": billet_form,
        "commentaire_form": commentaire_form
    })
