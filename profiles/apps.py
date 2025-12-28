"""
Ce module configure l'objet d'application (AppConfig) pour l'application 'profiles'.

L'AppConfig est utilisé par Django pour contenir les métadonnées de l'application
et pour définir des configurations spécifiques au démarrage.
"""


from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration de l'application 'profiles'.
    """
    name = 'profiles'
