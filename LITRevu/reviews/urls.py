from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('posts/', views.posts, name='posts'),
    path('billet/create/', views.show_billet_form, name='show-billet-form'),
    path('billet/create/submit/', views.create_billet, name='create-billet'),
    path('billet/edit/<int:billet_id>/', views.edit_billet, name='edit-billet'),
    path('billet/delete/<int:billet_id>/', views.delete_billet, name='delete-billet'),
    path('commentaire/create/', views.create_commentaire, name='commentaire-create'),
    path('commentaire/create/<int:billet_id>/', views.create_commentaire, name='commentaire-create'),
    path('commentaire/edit/<int:commentaire_id>/', views.edit_commentaire, name='edit-commentaire'),
    path('commentaire/delete/<int:commentaire_id>/', views.delete_commentaire, name='delete-commentaire'),
    path('billet-and-commentaire/create/', views.create_billet_and_commentaire, name='billet-and-commentaire-create'),
]