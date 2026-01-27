"""
Ce module contient les fonctions de vue principales pour le projet 'oc_lettings_site'.

Il est principalement responsable de la gestion et de l'affichage de la page d'accueil.
"""


from django.shortcuts import render
import sentry_sdk


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis, sem mi
# convallis eros, vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, eget
# consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Affiche la page d'accueil principale du site.

    Cette vue est le point d'entrée pour la route racine ('/').

    Args:
        request (HttpRequest): L'objet requête HTTP.

    Returns:
        HttpResponse: La page rendue 'index.html' du projet.
    """
    return render(request, 'index.html')


def custom_page_not_found(request, exception=None):
    """Gère les erreurs 404 et les envoie à Sentry"""
    sentry_sdk.capture_message("Page not found!", level="error")
    return render(request, '404.html', status=404)


# Handler pour les erreurs 500
def custom_server_error(request):
    """Gère les erreurs 500 et les envoie à Sentry"""
    sentry_sdk.capture_message("Internal server error!", level="error")
    return render(request, '500.html', status=500)


# test template personnalisée pour erreur 500
"""
def test_500(request):
    raise Exception("Test erreur 500")
"""
