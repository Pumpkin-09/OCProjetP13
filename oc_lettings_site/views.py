"""
Ce module contient les fonctions de vue principales pour le projet 'oc_lettings_site'.

Il est principalement responsable de la gestion et de l'affichage de la page d'accueil.
"""


from django.shortcuts import render


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


# test template personnalisée pour erreur 500
"""
def test_500(request):
    raise Exception("Test erreur 500")
"""