"""
Ce module contient les fonctions de vue pour l'application 'profiles'.

Il est responsable de l'affichage de la liste des profils utilisateur et des
pages de détail pour chaque profil individuel.
"""


from django.shortcuts import render
from profiles.models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Affiche la page d'index de l'application 'profiles'.

    Cette vue récupère tous les profils (Profile) de la base de données
    et les passe au template pour affichage.

    Args:
        request (HttpRequest): L'objet requête HTTP.

    Returns:
        HttpResponse: La page rendue 'profiles/index.html' avec la liste des profils.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra
# vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique
# senectus et netus et males
def profile(request, username):
    """
    Affiche la page de détail d'un profil utilisateur spécifique.

    Récupère un profil unique en recherchant le nom d'utilisateur associé
    au modèle User lié.

    Args:
        request (HttpRequest): L'objet requête HTTP.
        username (str): Le nom d'utilisateur (username) de l'utilisateur
                        dont on veut afficher le profil.

    Returns:
        HttpResponse: La page rendue 'profiles/profile.html' avec les détails
                      du profil.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
