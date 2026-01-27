"""
Définitions des chemins d'URL (routes) spécifiques à l'application 'lettings'.

Ce module mappe les requêtes HTTP aux fonctions de vue correspondantes dans
'lettings/views.py', définissant la liste des locations et la page de détail.
Ces chemins sont inclus via la fonction 'include' dans le ROOT_URLCONF du projet.
"""


from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='lettings_index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
