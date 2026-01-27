"""
Ce module contient les fonctions de vue pour l'application 'lettings'.

Il gère l'affichage de la liste complète des locations et des pages de détail
pour chaque bien immobilier.
"""


from django.shortcuts import render
from lettings.models import Letting
from django.http import Http404
import logging

logger = logging.getLogger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci luctus et
# ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Affiche la page d'index de l'application 'lettings'.

    Cette vue récupère toutes les fiches de location (Letting) de la base de données
    et les passe au template pour affichage.

    Args:
        request (HttpRequest): L'objet requête HTTP.

    Returns:
        HttpResponse: La page rendue 'lettings/index.html' avec la liste des locations.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium,
# purus urna vulputate arcu, vitae efficitur
# lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim, ac condimentum velit
# libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum. Ut quis urna pellentesque justo
# mattis ullamcorper ac non tellus. In tristique mauris eu velit fermentum, tempus pharetra
# est luctus. Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim,
# ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Affiche la page de détail d'une location spécifique.

    Récupère une fiche de location unique basée sur son ID.
    Si l'objet n'existe pas, Django lèvera une exception (généralement
    traitée comme une erreur 404).

    Args:
        request (HttpRequest): L'objet requête HTTP.
        letting_id (int): L'identifiant unique (ID) de la location à afficher.

    Returns:
        HttpResponse: La page rendue 'lettings/letting.html' avec les détails
                      de la location et son adresse.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f"Letting {letting_id} introuvable")
        raise Http404("Location non trouvée")
