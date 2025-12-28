"""
Ce module configure l'objet d'application (AppConfig) pour le projet principal 'oc_lettings_site'.

L'AppConfig est utilisé par Django pour contenir les métadonnées du projet 
et pour définir des configurations au moment où l'application est chargée.
"""


from django.apps import AppConfig


class OCLettingsSiteConfig(AppConfig):
    """
    Configuration de l'application 'oc_lettings_site'.
    """
    name = 'oc_lettings_site'
