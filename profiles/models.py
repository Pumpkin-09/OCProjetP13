"""
Ce module définit les modèles de données pour l'application profiles.

Il contient le modèle Profile qui permet d'étendre les informations stockées
pour chaque utilisateur Django standard (User). Ce modèle est configuré pour
pointer vers l'ancienne table de données 'oc_lettings_site_profile'.
"""


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente un profil utilisateur étendu.

    Ce modèle est lié à un utilisateur Django standard (User) via une relation
    OneToOne, permettant d'ajouter des champs spécifiques au profil, comme la
    ville favorite, sans modifier le modèle User par défaut. Il est lié à la
    table de base de données 'oc_lettings_site_profile'.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """
        Options de métadonnées pour le modèle Profile.
        Référence l'ancienne table de l'application 'oc_lettings_site'
        """
        db_table = 'oc_lettings_site_profile'

    def __str__(self):
        """
        Retourne le nom d'utilisateur (username) comme représentation textuelle.
        """
        return self.user.username
