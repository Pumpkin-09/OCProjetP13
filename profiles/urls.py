"""
Configuration des URLs pour l'application 'profiles'.

Ce module définit les routes URL permettant d'accéder aux vues
de l'application profiles. Les routes disponibles sont :
- '' : Liste de tous les profils
- '<username>/' : Détail d'un profil spécifique
"""


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
