"""
Configuration URL racine pour le projet oc_lettings_site (ROOT_URLCONF).

Ce fichier sert de point d'entrée pour toutes les requêtes HTTP. Il définit 
les routes principales (page d'accueil, administration) et utilise 'include()' 
pour déléguer la gestion des chemins '/lettings/' et '/profiles/' aux fichiers 
d'URL spécifiques de ces applications.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    # path('test-500/', views.test_500, name='test_500'), # test template personnalisée pour erreur 500
]
