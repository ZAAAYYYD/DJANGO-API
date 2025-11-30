# API Concessionnaire Auto/Moto

API Django REST Framework pour la gestion de concessionnaires automobiles et motos.

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
```

2. Activer l'environnement virtuel :
- Windows : `venv\Scripts\activate`
- Linux/Mac : `source venv/bin/activate`

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Lancer le serveur :
```bash
python manage.py runserver
```

## Endpoints API

### Concessionnaires

| Méthode | URL | Description |
|---------|-----|-------------|
| GET | `/api/concessionnaires/` | Liste des concessionnaires |
| GET | `/api/concessionnaires/<id>/` | Détails d'un concessionnaire |
| GET | `/api/concessionnaires/<id>/vehicules/` | Liste des véhicules d'un concessionnaire |
| GET | `/api/concessionnaires/<id>/vehicules/<id>/` | Détails d'un véhicule |

### Authentification (Bonus)

| Méthode | URL | Description |
|---------|-----|-------------|
| POST | `/api/users/` | Création d'un utilisateur |
| POST | `/api/token/` | Obtention d'un token JWT |
| POST | `/api/refresh_token/` | Rafraîchissement du token JWT |

## Modèles de données

### Concessionnaire
- `nom` : Nom du concessionnaire (max 64 caractères)
- `siret` : Numéro SIRET (14 caractères, non exposé par l'API)

### Véhicule
- `type` : Type de véhicule ("moto" ou "auto")
- `marque` : Marque du véhicule (max 64 caractères)
- `chevaux` : Puissance en chevaux
- `prix_ht` : Prix hors taxes
- `concessionnaire` : Lien vers le concessionnaire

