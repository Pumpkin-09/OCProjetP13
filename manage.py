"""
Script de ligne de commande principal pour les tâches d'administration du projet oc_lettings_site.

Ce fichier est le point d'entrée pour l'exécution de toutes les commandes
Django (comme runserver, makemigrations, shell, etc.). Il assure que les
paramètres Django sont correctement définis avant d'exécuter la commande demandée.
"""


import os
import sys


def main():
    """
    Définit les paramètres d'environnement pour Django et exécute la commande 
    demandée via l'interface de ligne de commande.
    
    Raises:
        ImportError: Si Django n'est pas installé ou l'environnement virtuel n'est 
                     pas activé, empêchant l'importation des outils de gestion.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
