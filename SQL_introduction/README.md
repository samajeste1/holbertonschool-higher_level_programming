# SQL - Introduction

Ce projet est une introduction à SQL et MySQL. Il couvre les concepts de base des bases de données relationnelles et les opérations SQL fondamentales.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Qu'est-ce qu'une base de données
- Qu'est-ce qu'une base de données relationnelle
- Que signifie SQL
- Qu'est-ce que MySQL
- Comment créer une base de données dans MySQL
- Que signifient DDL et DML
- Comment créer ou modifier une table
- Comment sélectionner des données d'une table
- Comment insérer, mettre à jour ou supprimer des données
- Qu'est-ce qu'une sous-requête
- Comment utiliser les fonctions MySQL

## Fichiers du projet

- `0-list_databases.sql` - Liste toutes les bases de données
- `1-create_database_if_missing.sql` - Crée la base de données hbtn_0c_0
- `2-remove_database.sql` - Supprime la base de données hbtn_0c_0
- `3-list_tables.sql` - Liste toutes les tables d'une base de données
- `4-first_table.sql` - Crée la table first_table
- `5-full_table.sql` - Affiche la description complète de first_table
- `6-list_values.sql` - Liste toutes les lignes de first_table
- `7-insert_value.sql` - Insère une nouvelle ligne dans first_table
- `8-count_89.sql` - Compte les enregistrements avec id = 89
- `9-full_creation.sql` - Crée second_table avec plusieurs lignes
- `10-top_score.sql` - Liste les enregistrements triés par score
- `11-best_score.sql` - Liste les enregistrements avec score >= 10
- `12-no_cheating.sql` - Met à jour le score de Bob
- `13-change_class.sql` - Supprime les enregistrements avec score <= 5
- `14-average.sql` - Calcule la moyenne des scores
- `15-groups.sql` - Compte les enregistrements par score
- `16-no_link.sql` - Liste les enregistrements où name n'est pas NULL

## Exigences

- Tous les fichiers doivent se terminer par une nouvelle ligne
- Toutes les requêtes SQL doivent avoir un commentaire juste avant
- Tous les fichiers doivent commencer par un commentaire décrivant la tâche
- Tous les mots-clés SQL doivent être en majuscules (SELECT, WHERE, etc.)

## Installation et utilisation

Pour utiliser ces scripts avec MySQL :

```bash
# Lister les bases de données
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p

# Créer une base de données
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p

# Utiliser une base de données spécifique
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Auteur

Holberton School

