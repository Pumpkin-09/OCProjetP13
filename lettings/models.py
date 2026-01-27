"""
Ce module définit les modèles de données pour l'application lettings.

Il contient les modèles Address et Letting qui permettent de gérer les adresses
physiques et les fiches de location. Ces modèles sont configurés pour pointer
vers les tables de données existantes de l'ancienne application oc_lettings_site.
"""


from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse postale complète.

    Ce modèle stocke les détails géographiques tels que le numéro, la rue,
    la ville et le code ISO du pays. Il est lié à la table de base de données
    'oc_lettings_site_address'.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        Options de métadonnées pour le modèle Address.
        Référence l'ancienne table de l'application 'oc_lettings_site'
        """
        db_table = 'oc_lettings_site_address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        """
        Retourne une représentation textuelle de l'adresse (numéro et rue).
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Représente une fiche de location (Letting).

    Une location possède un titre unique et est associée à une adresse
    via une relation OneToOne. Ce modèle est lié à la table de base de données
    'oc_lettings_site_letting'.
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """
        Options de métadonnées pour le modèle Letting.
        Référence l'ancienne table de l'application 'oc_lettings_site'
        """
        db_table = 'oc_lettings_site_letting'

    def __str__(self):
        """
        Retourne le titre de la location comme représentation textuelle.
        """
        return self.title
