# Python - Everything is object

Ce projet explore en profondeur le concept fondamental de Python : **tout est un objet**. Il couvre les différences entre objets mutables et immutables, les références, les alias, et comment Python traite les variables.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Qu'est-ce qu'un objet
- Quelle est la différence entre une classe et un objet ou instance
- Quelle est la différence entre un objet immutable et un objet mutable
- Qu'est-ce qu'une référence
- Qu'est-ce qu'une assignation
- Qu'est-ce qu'un alias
- Comment savoir si deux variables sont identiques
- Comment savoir si deux variables sont liées au même objet
- Comment afficher l'identifiant d'une variable (qui est l'adresse mémoire dans l'implémentation CPython)
- Qu'est-ce que mutable et immutable
- Quels sont les types mutables intégrés
- Quels sont les types immutables intégrés
- Comment Python passe les variables aux fonctions

## Concepts clés

### Objets et références

En Python, tout est un objet. Les variables sont des références (pointeurs) vers des objets en mémoire.

```python
a = 89
b = a  # b référence le même objet que a
```

### Identité vs Égalité

- **`==`** : Compare les **valeurs** (égalité)
- **`is`** : Compare les **identités** (même objet en mémoire)

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True - même contenu
print(a is b)  # False - objets différents
```

### Types immutables

Les objets immutables ne peuvent pas être modifiés après leur création :
- `int`, `float`, `str`, `tuple`, `frozenset`, `bool`, `None`

```python
a = 1
b = a
a = 2
print(b)  # 1 - b référence toujours l'objet 1
```

### Types mutables

Les objets mutables peuvent être modifiés après leur création :
- `list`, `dict`, `set`, `bytearray`

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4] - l2 référence le même objet
```

### Interning

Python "interne" certains objets pour optimiser la mémoire :
- Petits entiers (-5 à 256)
- Chaînes courtes (dans certaines conditions)
- Tuples vides

```python
a = 89
b = 89
print(a is b)  # True - même objet (interning)

a = 257
b = 257
print(a is b)  # Peut être False selon l'implémentation
```

### Passage d'arguments aux fonctions

Python passe les arguments **par référence** :
- Pour les objets immutables : la fonction reçoit une référence, mais ne peut pas modifier l'objet original
- Pour les objets mutables : la fonction peut modifier l'objet original

```python
def increment(n):
    n += 1  # Crée un nouvel objet, n'est pas modifié en place

a = 1
increment(a)
print(a)  # 1 - non modifié

def append_item(lst):
    lst.append(4)  # Modifie l'objet en place

l = [1, 2, 3]
append_item(l)
print(l)  # [1, 2, 3, 4] - modifié
```

### Opérations sur les listes

- **`l1 = l1 + [4]`** : Crée un **nouvel objet** (nouvelle liste)
- **`l1 += [4]`** ou **`l1.append(4)`** : Modifie l'objet **en place**

```python
l1 = [1, 2, 3]
l2 = l1
id1 = id(l1)

l1 = l1 + [4]  # Nouvel objet
print(id(l1) == id1)  # False

l1 = [1, 2, 3]
l2 = l1
id1 = id(l1)

l1 += [4]  # Modification en place
print(id(l1) == id1)  # True
```

### Tuples

Les tuples sont créés avec des virgules, pas des parenthèses :

```python
a = ()        # Tuple vide
a = (1, 2)    # Tuple avec 2 éléments
a = (1)       # Pas un tuple ! C'est un int
a = (1,)      # Tuple avec 1 élément (virgule requise)
```

## Fichiers du projet

### Fichiers de réponses (0-28)
- `0-answer.txt` à `28-answer.txt` - Réponses aux questions théoriques

### Fichiers Python
- `19-copy_list.py` - Fonction pour copier une liste

## Fonctions utiles

### `type()`
Retourne le type d'un objet :
```python
type(42)  # <class 'int'>
type([1, 2, 3])  # <class 'list'>
```

### `id()`
Retourne l'identifiant unique d'un objet (adresse mémoire en CPython) :
```python
a = [1, 2, 3]
id(a)  # 139926795932424 (exemple)
```

### `is` vs `==`
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # True - même contenu
a is b  # False - objets différents

c = a
a is c  # True - même objet
```

## Exigences

- Tous les fichiers `.txt` doivent contenir une seule ligne
- Pas de shebang dans les fichiers `.txt`
- Tous les fichiers doivent se terminer par une nouvelle ligne
- Les fichiers Python doivent avoir `#!/usr/bin/python3` en première ligne
- Code conforme à pycodestyle (version 2.7.*)
- Tous les fichiers Python doivent être exécutables

## Exemples de réponses

### Question 14 : List append
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)  # [1, 2, 3, 4]
```
**Réponse** : `[1, 2, 3, 4]` - `l1` et `l2` référencent le même objet mutable.

### Question 15 : List add
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)  # [1, 2, 3]
```
**Réponse** : `[1, 2, 3]` - `l1 = l1 + [4]` crée un nouvel objet, `l2` référence toujours l'ancien.

### Question 27 : Same or not?
```python
a = [1, 2, 3, 4]
id(a)  # 139926795932424
a = a + [5]  # Crée un nouvel objet
id(a)  # Différent !
```
**Réponse** : `No` - `a + [5]` crée un nouvel objet.

### Question 28 : Same or not?
```python
a = [1, 2, 3]
id(a)  # 139926795932424
a += [4]  # Modification en place
id(a)  # Même id !
```
**Réponse** : `Yes` - `+=` modifie l'objet en place.

## Ressources

- [9.10. Objects and values](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [9.11. Aliasing](https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)
- [Immutable vs mutable types](https://docs.python.org/3/reference/datamodel.html)
- [9.12. Cloning lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Python tuples: immutable but potentially changing](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

## Auteur

Holberton School



