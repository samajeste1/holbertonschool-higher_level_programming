# JavaScript - Warm up

Ce projet est une introduction au JavaScript, couvrant les concepts de base du langage : variables, types de données, opérateurs, structures de contrôle, fonctions et objets.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Pourquoi la programmation JavaScript est géniale
- Comment exécuter un script JavaScript
- Comment créer des variables et constantes
- Quelles sont les différences entre var, const et let
- Quels sont tous les types de données disponibles en JavaScript
- Comment utiliser les instructions if, if ... else
- Comment utiliser les commentaires
- Comment affecter des valeurs aux variables
- Comment utiliser les boucles while et for
- Comment utiliser les instructions break et continue
- Qu'est-ce qu'une fonction et comment utiliser les fonctions
- Ce que retourne une fonction qui n'utilise aucune instruction return
- Portée des variables
- Quels sont les opérateurs arithmétiques et comment les utiliser
- Comment manipuler un dictionnaire
- Comment importer un fichier

## Fichiers du projet

### Scripts de base (0-5)
- `0-javascript_is_amazing.js` - Affiche "JavaScript is amazing" avec une constante
- `1-multi_languages.js` - Affiche 3 lignes de texte
- `2-arguments.js` - Affiche un message selon le nombre d'arguments
- `3-value_argument.js` - Affiche le premier argument passé
- `4-concat.js` - Concatène deux arguments avec " is "
- `5-to_integer.js` - Convertit et affiche le premier argument en entier

### Scripts avec boucles et fonctions (6-9)
- `6-multi_languages_loop.js` - Affiche 3 lignes en utilisant un tableau et une boucle
- `7-multi_c.js` - Affiche "C is fun" x fois
- `8-square.js` - Affiche un carré de X
- `9-add.js` - Additionne deux entiers avec une fonction

### Scripts avancés (10-13)
- `10-factorial.js` - Calcule et affiche une factorielle de manière récursive
- `11-second_biggest.js` - Trouve le deuxième plus grand entier dans les arguments
- `12-object.js` - Modifie la valeur d'un objet
- `13-add.js` - Fonction exportable pour additionner deux entiers

## Concepts clés

### Variables et constantes
- `const` : constante, ne peut pas être réassignée
- `let` : variable avec portée de bloc
- `var` : **NE PAS UTILISER** (ancien standard)

### Types de données
- `Number` : nombres entiers et décimaux
- `String` : chaînes de caractères
- `Boolean` : true/false
- `undefined` : valeur non définie
- `null` : valeur nulle
- `Object` : objets et tableaux

### Structures de contrôle
- `if/else` : conditions
- `for` : boucle avec compteur
- `while` : boucle conditionnelle
- `break` : sortir d'une boucle
- `continue` : passer à l'itération suivante

### Fonctions
```javascript
function add(a, b) {
  return a + b;
}
```

### Modules
```javascript
module.exports = { add };
```

## Exigences

- Tous les fichiers doivent commencer par `#!/usr/bin/node`
- Tous les fichiers doivent se terminer par une nouvelle ligne
- Tous les fichiers doivent être exécutables (`chmod +x`)
- Code conforme à semistandard (version 16.x.x)
- Pas d'utilisation de `var`, seulement `const` et `let`
- Utiliser `console.log()` pour l'output

## Installation

### Installer Node.js 14
```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Installer semistandard
```bash
sudo npm install semistandard --global
```

## Utilisation

### Exécuter un script
```bash
./0-javascript_is_amazing.js
```

### Vérifier le style
```bash
semistandard 0-javascript_is_amazing.js
```

### Exemples d'exécution
```bash
# Script avec arguments
./2-arguments.js Best School
# Output: Arguments found

# Script avec fonction
./9-add.js 13 89
# Output: 102

# Script avec module
node 13-main.js
# Output: 8
```

## Notes importantes

- `process.argv` : tableau contenant les arguments de la ligne de commande
  - `process.argv[0]` : chemin de Node.js
  - `process.argv[1]` : chemin du script
  - `process.argv[2]` et suivants : arguments passés au script

- Conversion de types :
  - `parseInt()` : convertir en entier
  - `isNaN()` : vérifier si ce n'est pas un nombre

- Portée des variables :
  - Variables `const` et `let` : portée de bloc
  - Variables `var` : portée de fonction (à éviter)

## Auteur

Holberton School



