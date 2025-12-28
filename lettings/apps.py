"""
Ce module configure l'objet d'application (AppConfig) pour l'application 'lettings'.

L'AppConfig est un mécanisme standard de Django pour définir les métadonnées de l'application
et pour exécuter des configurations spécifiques lors du chargement de l'application.
"""


from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration de l'application 'lettings'.
    """
    name = 'lettings'
