# Python - Object-relational mapping

Ce projet explore deux approches pour interagir avec des bases de données MySQL depuis Python :
1. **MySQLdb** : Connexion directe et exécution de requêtes SQL
2. **SQLAlchemy** : ORM (Object-Relational Mapping) pour une abstraction complète

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Comment se connecter à une base de données MySQL depuis un script Python
- Comment sélectionner des lignes dans une table MySQL depuis un script Python
- Comment insérer des lignes dans une table MySQL depuis un script Python
- Ce que signifie ORM
- Comment mapper une classe Python à une table MySQL

## Structure du projet

### Partie 1 : MySQLdb (0-5)

**Scripts de base :**
- `0-select_states.py` - Liste tous les états de la base de données
- `1-filter_states.py` - Filtre les états commençant par 'N'
- `2-my_filter_states.py` - Filtre par nom d'état (vulnérable à SQL injection)
- `3-my_safe_filter_states.py` - Filtre par nom d'état (sécurisé contre SQL injection)
- `4-cities_by_state.py` - Liste toutes les villes avec leur état
- `5-filter_cities.py` - Liste les villes d'un état spécifique

**Concepts clés :**
- Connexion à MySQL avec `MySQLdb.connect()`
- Utilisation de curseurs pour exécuter des requêtes
- Requêtes paramétrées pour éviter les injections SQL
- Jointures SQL pour récupérer des données de plusieurs tables

### Partie 2 : SQLAlchemy (6-14)

**Modèles :**
- `model_state.py` - Définition de la classe `State` (hérite de `Base`)
- `model_city.py` - Définition de la classe `City` (hérite de `Base`)

**Scripts de base :**
- `6-model_state.py` - Crée la table `states` dans la base de données
- `7-model_state_fetch_all.py` - Liste tous les objets `State`
- `8-model_state_fetch_first.py` - Affiche le premier objet `State`
- `9-model_state_filter_a.py` - Filtre les `State` contenant la lettre 'a'
- `10-model_state_my_get.py` - Trouve un `State` par nom

**Scripts de modification :**
- `11-model_state_insert.py` - Ajoute un nouvel état "Louisiana"
- `12-model_state_update_id_2.py` - Met à jour l'état avec id=2
- `13-model_state_delete_a.py` - Supprime les états contenant 'a'
- `14-model_city_fetch_by_state.py` - Liste toutes les villes avec leur état

**Concepts clés :**
- ORM (Object-Relational Mapping) : abstraction de la base de données
- Classes SQLAlchemy héritant de `Base`
- Sessions pour gérer les transactions
- Requêtes orientées objet au lieu de SQL brut

## Différence entre MySQLdb et SQLAlchemy

### Avec MySQLdb (SQL brut) :
```python
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
```

### Avec SQLAlchemy (ORM) :
```python
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
```

## Installation

### Prérequis
```bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
```

### Installer MySQLdb
```bash
sudo pip3 install mysqlclient==2.0.3
```

### Installer SQLAlchemy
```bash
sudo pip3 install SQLAlchemy==1.4.22
```

## Utilisation

### Préparer les bases de données

**Pour les scripts 0-3 (hbtn_0e_0_usa) :**
```bash
cat 0-select_states.sql | mysql -uroot -p
```

**Pour les scripts 4-5 (hbtn_0e_4_usa) :**
```bash
cat 4-cities_by_state.sql | mysql -uroot -p
```

**Pour les scripts 6-13 (hbtn_0e_6_usa) :**
```bash
cat 6-model_state.sql | mysql -uroot -p
cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
```

**Pour le script 14 (hbtn_0e_14_usa) :**
```bash
cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
```

### Exécuter les scripts

**Scripts MySQLdb :**
```bash
./0-select_states.py root root hbtn_0e_0_usa
./1-filter_states.py root root hbtn_0e_0_usa
./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
./4-cities_by_state.py root root hbtn_0e_4_usa
./5-filter_cities.py root root hbtn_0e_4_usa Texas
```

**Scripts SQLAlchemy :**
```bash
./6-model_state.py root root hbtn_0e_6_usa
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
./8-model_state_fetch_first.py root root hbtn_0e_6_usa
./9-model_state_filter_a.py root root hbtn_0e_6_usa
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
./11-model_state_insert.py root root hbtn_0e_6_usa
./12-model_state_update_id_2.py root root hbtn_0e_6_usa
./13-model_state_delete_a.py root root hbtn_0e_6_usa
./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
```

## Sécurité : Protection contre les injections SQL

### ❌ Vulnérable (format) :
```python
cur.execute("SELECT * FROM states WHERE name = '{}'".format(state_name))
```

### ✅ Sécurisé (requête paramétrée) :
```python
cur.execute("SELECT * FROM states WHERE name = %s", (state_name,))
```

Avec SQLAlchemy, les requêtes sont automatiquement protégées :
```python
session.query(State).filter(State.name == state_name).first()
```

## Exigences

- Tous les fichiers doivent se terminer par une nouvelle ligne
- La première ligne doit être `#!/usr/bin/python3`
- Tous les fichiers doivent être exécutables (`chmod +x`)
- Code conforme à pycodestyle (version 2.7.*)
- Documentation complète pour tous les modules, classes et fonctions
- Pas d'utilisation de `execute()` avec SQLAlchemy (utiliser l'ORM)

## Auteur

Holberton School



