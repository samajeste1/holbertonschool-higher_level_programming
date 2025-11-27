# Python - Server-Side Rendering

Ce projet explore le rendu côté serveur (Server-Side Rendering) en utilisant Python et Flask, avec le moteur de templating Jinja pour créer des applications web dynamiques, efficaces et optimisées pour le SEO.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Comprendre les concepts du rendu côté serveur et comment il diffère du rendu côté client
- Apprendre les avantages de l'utilisation du rendu côté serveur dans le développement web
- Implémenter SSR en Python en utilisant le framework Flask
- Utiliser le moteur de templating Jinja pour générer dynamiquement des pages HTML
- Lire et afficher des données depuis diverses sources (JSON, CSV, SQLite)
- Gérer le contenu dynamique et les entrées utilisateur dans les applications web

## Structure du projet

### Fichiers Python
- `task_00_intro.py` - Fonction de templating simple pour générer des invitations
- `task_01_jinja.py` - Application Flask basique avec templates Jinja
- `task_02_logic.py` - Templates dynamiques avec boucles et conditions
- `task_03_files.py` - Lecture et affichage de données depuis JSON/CSV
- `task_04_db.py` - Extension pour inclure SQLite comme source de données
- `create_database.py` - Script pour créer et peupler la base de données SQLite

### Templates HTML
- `templates/index.html` - Page d'accueil
- `templates/about.html` - Page À propos
- `templates/contact.html` - Page Contact
- `templates/header.html` - En-tête réutilisable
- `templates/footer.html` - Pied de page réutilisable
- `templates/items.html` - Liste d'éléments dynamiques
- `templates/product_display.html` - Affichage de produits

### Fichiers de données
- `template.txt` - Template pour les invitations
- `items.json` - Liste d'éléments pour Task 2
- `products.json` - Données produits au format JSON
- `products.csv` - Données produits au format CSV
- `products.db` - Base de données SQLite (créée avec create_database.py)

## Tâches

### Task 0: Creating a Simple Templating Program
Fonction `generate_invitations` qui génère des fichiers d'invitation personnalisés à partir d'un template et d'une liste d'objets.

**Fonctionnalités :**
- Vérification des types d'entrée
- Gestion des templates vides
- Gestion des listes vides
- Remplacement des valeurs manquantes par "N/A"
- Génération de fichiers de sortie numérotés

### Task 1: Creating a Basic HTML Template in Flask
Application Flask basique avec templates Jinja incluant des composants réutilisables (header, footer).

**Fonctionnalités :**
- Routes pour home, about, contact
- Templates réutilisables avec `{% include %}`
- Navigation entre les pages

### Task 2: Creating a Dynamic Template with Loops and Conditions
Templates dynamiques utilisant les boucles et conditions Jinja pour afficher des données depuis un fichier JSON.

**Fonctionnalités :**
- Lecture de données JSON
- Boucles `{% for %}` pour itérer sur les éléments
- Conditions `{% if %}` pour gérer les listes vides

### Task 3: Displaying Data from JSON or CSV Files
Application Flask qui lit et affiche des données produits depuis JSON ou CSV selon un paramètre de requête.

**Fonctionnalités :**
- Support de plusieurs sources de données (JSON, CSV)
- Filtrage par ID optionnel
- Gestion d'erreurs pour sources invalides
- Affichage dans un tableau HTML

### Task 4: Extending Dynamic Data Display to Include SQLite
Extension de Task 3 pour inclure SQLite comme source de données supplémentaire.

**Fonctionnalités :**
- Support de JSON, CSV et SQLite
- Requêtes SQL pour récupérer des données
- Même interface utilisateur pour toutes les sources

## Installation

### Prérequis
```bash
pip install Flask
```

### Créer la base de données
```bash
python3 create_database.py
```

## Utilisation

### Lancer l'application Flask
```bash
python3 task_01_jinja.py
# ou
python3 task_02_logic.py
# ou
python3 task_03_files.py
# ou
python3 task_04_db.py
```

L'application sera accessible sur `http://localhost:5000`

### Tester Task 0
```python
from task_00_intro import generate_invitations

with open('template.txt', 'r') as file:
    template_content = file.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference", 
     "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", 
     "event_date": "2023-08-20", "event_location": "San Francisco"}
]

generate_invitations(template_content, attendees)
```

### Tester les routes
- `http://localhost:5000/` - Page d'accueil
- `http://localhost:5000/about` - Page À propos
- `http://localhost:5000/contact` - Page Contact
- `http://localhost:5000/items` - Liste d'éléments (Task 2)
- `http://localhost:5000/products?source=json` - Produits depuis JSON
- `http://localhost:5000/products?source=csv` - Produits depuis CSV
- `http://localhost:5000/products?source=sql` - Produits depuis SQLite
- `http://localhost:5000/products?source=json&id=1` - Produit spécifique

## Concepts clés

### Jinja Templating
```jinja
{% include 'header.html' %}
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
{% if condition %}
    <p>Condition is true</p>
{% endif %}
```

### Flask Routes
```python
@app.route('/path')
def function_name():
    return render_template('template.html', data=data)
```

### Lecture de fichiers
- **JSON** : `json.load(file)`
- **CSV** : `csv.DictReader(file)`
- **SQLite** : `sqlite3.connect('database.db')`

## Exigences

- Python 3.x
- Flask installé
- Tous les fichiers doivent se terminer par une nouvelle ligne
- Code conforme aux standards Python (PEP 8)
- Gestion d'erreurs appropriée

## Ressources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python JSON Documentation](https://docs.python.org/3/library/json.html)
- [Python CSV Documentation](https://docs.python.org/3/library/csv.html)
- [Python SQLite Documentation](https://docs.python.org/3/library/sqlite3.html)

## Auteur

Holberton School



