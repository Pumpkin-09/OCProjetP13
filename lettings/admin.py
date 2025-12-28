"""
Ce module configure l'interface d'administration de Django pour l'application 'lettings'.

Il enregistre les modèles Letting et Address afin qu'ils puissent être gérés 
via l'interface d'administration du site.
"""


from django.contrib import admin

from .models import Letting
from .models import Address


admin.site.register(Letting)
admin.site.register(Address)
