# SQL - More queries

Ce projet approfondit les concepts SQL introduits précédemment, en se concentrant sur la gestion des utilisateurs, les contraintes de tables, les clés primaires et étrangères, ainsi que les requêtes avancées avec JOIN et sous-requêtes.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Comment créer un nouvel utilisateur MySQL
- Comment gérer les privilèges d'un utilisateur pour une base de données ou une table
- Qu'est-ce qu'une PRIMARY KEY
- Qu'est-ce qu'une FOREIGN KEY
- Comment utiliser les contraintes NOT NULL et UNIQUE
- Comment récupérer des données de plusieurs tables dans une seule requête
- Qu'est-ce qu'une sous-requête
- Qu'est-ce que JOIN et UNION

## Fichiers du projet

### Gestion des utilisateurs (0-2)
- `0-privileges.sql` - Liste les privilèges des utilisateurs user_0d_1 et user_0d_2
- `1-create_user.sql` - Crée l'utilisateur user_0d_1 avec tous les privilèges
- `2-create_read_user.sql` - Crée la base hbtn_0d_2 et l'utilisateur user_0d_2 avec seulement SELECT

### Contraintes de tables (3-5)
- `3-force_name.sql` - Crée la table force_name avec name NOT NULL
- `4-never_empty.sql` - Crée la table id_not_null avec id par défaut 1
- `5-unique_id.sql` - Crée la table unique_id avec id unique

### Bases de données avec clés (6-7)
- `6-states.sql` - Crée la base hbtn_0d_usa et la table states avec PRIMARY KEY
- `7-cities.sql` - Crée la table cities avec FOREIGN KEY vers states

### Requêtes avec sous-requêtes et JOIN (8-9)
- `8-cities_of_california_subquery.sql` - Liste les villes de Californie (sans JOIN)
- `9-cities_by_state_join.sql` - Liste toutes les villes avec leur état (avec JOIN)

### Requêtes sur tvshows (10-12)
- `10-genre_id_by_show.sql` - Liste les shows avec au moins un genre
- `11-genre_id_all_shows.sql` - Liste tous les shows avec genre (NULL si pas de genre)
- `12-no_genre.sql` - Liste les shows sans genre

### Requêtes avancées (13-16)
- `13-count_shows_by_genre.sql` - Compte les shows par genre
- `14-my_genres.sql` - Liste les genres de Dexter
- `15-comedy_only.sql` - Liste les shows Comedy
- `16-shows_by_genre.sql` - Liste tous les shows avec leurs genres

## Concepts clés

### Contraintes SQL
- **NOT NULL** : Empêche une colonne d'avoir des valeurs NULL
- **UNIQUE** : Garantit que toutes les valeurs d'une colonne sont différentes
- **PRIMARY KEY** : Identifie de manière unique chaque ligne d'une table
- **FOREIGN KEY** : Référence une PRIMARY KEY dans une autre table

### Types de JOIN
- **INNER JOIN** : Retourne uniquement les lignes qui ont des correspondances dans les deux tables
- **LEFT JOIN** : Retourne toutes les lignes de la table de gauche, même sans correspondance

### Sous-requêtes
Les sous-requêtes permettent d'utiliser le résultat d'une requête dans une autre requête, souvent dans une clause WHERE.

## Exigences

- Tous les fichiers doivent se terminer par une nouvelle ligne
- Toutes les requêtes SQL doivent avoir un commentaire juste avant
- Tous les fichiers doivent commencer par un commentaire décrivant la tâche
- Tous les mots-clés SQL doivent être en majuscules (SELECT, WHERE, etc.)

## Installation et utilisation

Pour utiliser ces scripts avec MySQL :

```bash
# Lister les privilèges d'un utilisateur
cat 0-privileges.sql | mysql -hlocalhost -uroot -p

# Créer un utilisateur
cat 1-create_user.sql | mysql -hlocalhost -uroot -p

# Créer une table avec contraintes
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2

# Exécuter des requêtes sur une base de données
cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

## Import de la base de données hbtn_0d_tvshows

Pour importer la base de données de démonstration :

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

## Auteur

Holberton School



