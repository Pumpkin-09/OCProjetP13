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

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('sentry-debug/', trigger_error),
    # path('test-500/', views.test_500, name='test_500'), # test template personnalisée pour erreur 500
]

handler404 = 'oc_lettings_site.views.custom_page_not_found'
handler500 = 'oc_lettings_site.views.custom_server_error'
