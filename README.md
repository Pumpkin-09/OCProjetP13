# Projet P13: Mettez à l'échelle une application Django en utilisant une architecture modulaire


## 🌐 Liens rapides

- **Application en production** : https://ocprojetp13.onrender.com/
- **Documentation complète** : https://ocprojetp13.readthedocs.io/fr/latest/
- **Image Docker** : https://hub.docker.com/r/pumpkin99/oc-lettings/tags


## ✨ Fonctionnalités

- 🏠 **Gestion de locations** : Consultation des annonces de location disponibles
- 👤 **Profils utilisateurs** : Gestion et affichage des profils utilisateurs
- 🔐 **Interface d'administration** : Panneau d'administration Django pour la gestion des données
- 🐛 **Monitoring** : Intégration Sentry pour le suivi des erreurs


## 🛠 Technologies

- **Backend** : Django 3.0, Python 3.11
- **Base de données** : SQLite
- **Conteneurisation** : Docker
- **CI/CD** : GitHub Actions
- **Déploiement** : Render
- **Monitoring** : Sentry
- **Documentation** : Sphinx, Read the Docs
- **Tests** : pytest, pytest-django, pytest-cov
- **Quality** : flake8


## 🚀 Installation locale

### Prérequis

- Python 3.11
- pip
- virtualenv (recommandé)


### Étapes

1. **Cloner le repository**

```bash
git clone https://github.com/Pumpkin-09/Python-OC-Lettings-FR.git
cd Python-OC-Lettings-FR
```

2. **Créer et activer un environnement virtuel**

```bash
# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Configurer les variables d'environnement**

Créez un fichier `.env` à la racine du projet :

```env
SECRET_KEY=votre-clé-secrète-django
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DSN_SENTRY=votre-dsn-sentry  # Optionnel
```

5. **Appliquer les migrations**

```bash
python manage.py migrate
```

6. **Créer un superutilisateur (optionnel)**

```bash
python manage.py createsuperuser
```

7. **Lancer le serveur de développement**

```bash
python manage.py runserver
```

L'application est accessible sur : `http://localhost:8000`

## 🐳 Utilisation avec Docker

### Avec Docker Hub

```bash
# Télécharger et lancer l'image depuis Docker Hub
docker run -d -p 8000:8000 \
  -e SECRET_KEY=votre-secret-key \
  -e DEBUG=False \
  -e ALLOWED_HOSTS=localhost,127.0.0.1 \
  pumpkin99/oc-lettings:latest
```

### Avec un fichier .env

```bash
docker run -d -p 8000:8000 \
  --env-file .env \
  pumpkin99/oc-lettings:latest
```

### Build local

```bash
# Construire l'image
docker build -t oc-lettings .

# Lancer le conteneur
docker run -d -p 8000:8000 \
  --env-file .env \
  oc-lettings
```

L'application est accessible sur : `http://localhost:8000`

## 🧪 Tests

### Lancer tous les tests

```bash
pytest -v
```

### Tests avec couverture

```bash
pytest --cov=. --cov-report=term-missing
```

### Linting

```bash
flake8 .
```

## 📦 Déploiement

### Pipeline CI/CD

Le projet utilise GitHub Actions pour automatiser :

1. **Tests** : Exécution des tests et vérification de la couverture (>80%)
2. **Linting** : Vérification du code avec flake8
3. **Build** : Construction et test de l'image Docker
4. **Push** : Publication de l'image sur Docker Hub (nécessite les secrets)
5. **Deploy** : Déploiement automatique sur Render (nécessite le webhook)

Le pipeline se déclenche automatiquement sur :
- Push sur la branche `main`
- Pull requests vers `main`


### Déployer votre propre version

Si vous souhaitez déployer votre propre version de l'application :

#### 1. Configuration Docker Hub

1. Créez un compte sur [Docker Hub](https://hub.docker.com/)
2. Créez un repository (ex: `votre-username/oc-lettings`)
3. Dans les secrets GitHub de votre fork, ajoutez :
   - `DOCKER_USERNAME` : votre nom d'utilisateur Docker Hub
   - `DOCKER_PASSWORD` : votre token Docker Hub

#### 2. Configuration Render

1. Créez un compte sur [Render](https://render.com/)
2. Créez un nouveau **Web Service**
3. Choisissez "Deploy from Docker Hub"
4. Spécifiez votre image : `votre-username/oc-lettings:latest`
5. Configurez les variables d'environnement :
   - `SECRET_KEY` : votre clé secrète Django
   - `DEBUG` : `False`
   - `ALLOWED_HOSTS` : votre domaine Render
   - `DSN_SENTRY` : (optionnel) votre DSN Sentry
6. Dans les paramètres, copiez le **Deploy Hook URL**
7. Ajoutez ce webhook dans les secrets GitHub : `DEPLOY_HOOK`

#### 3. Configuration des secrets GitHub

Pour que le pipeline CI/CD fonctionne, vous devez configurer les secrets dans votre repository GitHub :

1. Allez dans votre repository GitHub
2. Cliquez sur **Settings** > **Secrets and variables** > **Actions**
3. Cliquez sur **New repository secret**
4. Ajoutez les secrets suivants :

| Nom du secret | Description | Exemple |
|---------------|-------------|---------|
| `SECRET_KEY` | Clé secrète Django pour les tests | < votre clé secrete > |
| `DOCKER_USERNAME` | Nom d'utilisateur Docker Hub | <votre-username> |
| `DOCKER_PASSWORD` | Token Docker Hub (pas le mot de passe) | `dckr_pat_xxx...` |
| `DEPLOY_HOOK` | URL du webhook Render | < votre deploy-hook render > |

**Note importante** : Pour `DOCKER_PASSWORD`, utilisez un **Access Token** Docker Hub plutôt que votre mot de passe :
- Allez sur [Docker Hub](https://hub.docker.com/) > Account Settings > Security > New Access Token
- Créez un token avec les permissions "Read, Write, Delete"
- Copiez le token et utilisez-le comme `DOCKER_PASSWORD`

#### 4. Modifier le workflow GitHub Actions

Dans `.github/workflows/ci.yml`, modifiez la variable `IMAGE_NAME` :
```yaml
env:
  REGISTRY: docker.io
  IMAGE_NAME: ${{ secrets.DOCKER_USERNAME }}/oc-lettings  # Utilisera votre username
```

Une fois configuré, chaque push sur `main` déclenchera automatiquement :
- La construction de l'image Docker
- Le push vers votre Docker Hub
- Le déploiement sur votre instance Render

### Déploiement manuel sur Render

L'application est déployée automatiquement sur Render via un webhook. Chaque push sur `main` déclenche un nouveau déploiement.

## 📚 Documentation

### Consulter la documentation

La documentation complète est disponible sur [Read the Docs](https://ocprojetp13.readthedocs.io/fr/latest/).

### Générer la documentation localement

```bash
cd docs
make html
```

La documentation générée se trouve dans `docs/_build/html/index.html`.

Pour la visualiser :

```bash
cd docs/_build/html
python -m http.server 8000
```

Puis ouvrez `http://localhost:8000` dans votre navigateur.
