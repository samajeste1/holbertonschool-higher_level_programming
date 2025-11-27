# HBnB - Business Logic and API (Part 2)

Ce projet implémente la couche Business Logic et les endpoints API pour l'application HBnB (clone d'AirBnB).

## Objectifs

- Mettre en place la structure du projet avec une architecture modulaire
- Implémenter la couche Business Logic (User, Place, Review, Amenity)
- Implémenter les endpoints RESTful API avec Flask et flask-restx
- Utiliser le pattern Facade pour simplifier la communication entre les couches
- Implémenter un repository en mémoire pour la persistance

## Structure du projet

```
part2/
├── app/
│   ├── __init__.py          # Application Factory
│   ├── config.py             # Configuration
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py      # Endpoints utilisateurs
│   │       ├── places.py     # Endpoints places
│   │       ├── reviews.py    # Endpoints reviews
│   │       └── amenities.py  # Endpoints amenities
│   ├── business_logic/
│   │   ├── __init__.py
│   │   ├── base_model.py     # Classe de base
│   │   ├── user.py           # Modèle User
│   │   ├── place.py          # Modèle Place
│   │   ├── review.py         # Modèle Review
│   │   └── amenity.py        # Modèle Amenity
│   ├── persistence/
│   │   ├── __init__.py
│   │   ├── repository.py     # Interface repository
│   │   └── in_memory_repository.py  # Implémentation en mémoire
│   └── facade/
│       ├── __init__.py
│       └── facade.py         # Pattern Facade
├── requirements.txt
└── README.md
```

## Tâches

### Task 0: Project Setup and Package Initialization
- Créer la structure des dossiers
- Configurer Flask Application Factory
- Implémenter le repository en mémoire
- Mettre en place le pattern Facade

### Task 1: Core Business Logic Classes
- Implémenter les classes User, Place, Review, Amenity
- Définir les attributs et méthodes
- Implémenter les relations entre entités

### Task 2: User Endpoints
- POST /api/v1/users/ - Créer un utilisateur
- GET /api/v1/users/ - Lister les utilisateurs
- GET /api/v1/users/<id> - Obtenir un utilisateur
- PUT /api/v1/users/<id> - Mettre à jour un utilisateur

### Task 3: Amenity Endpoints
- POST /api/v1/amenities/ - Créer une amenity
- GET /api/v1/amenities/ - Lister les amenities
- GET /api/v1/amenities/<id> - Obtenir une amenity
- PUT /api/v1/amenities/<id> - Mettre à jour une amenity

### Task 4: Place Endpoints
- POST /api/v1/places/ - Créer un place
- GET /api/v1/places/ - Lister les places
- GET /api/v1/places/<id> - Obtenir un place
- PUT /api/v1/places/<id> - Mettre à jour un place

### Task 5: Review Endpoints
- POST /api/v1/reviews/ - Créer un review
- GET /api/v1/reviews/ - Lister les reviews
- GET /api/v1/reviews/<id> - Obtenir un review
- PUT /api/v1/reviews/<id> - Mettre à jour un review
- DELETE /api/v1/reviews/<id> - Supprimer un review

### Task 6: Testing and Validation
- Implémenter la validation
- Tester avec cURL
- Générer la documentation Swagger
- Créer des tests unitaires

## Installation

```bash
pip install -r requirements.txt
```

## Exécution

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

## Ressources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-RESTx Documentation](https://flask-restx.readthedocs.io/)
- [Facade Pattern](https://refactoring.guru/design-patterns/facade)

## Auteur

Holberton School - Team: Allan, Bony, Rattler



