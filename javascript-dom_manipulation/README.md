# JavaScript DOM Manipulation

Ce projet explore la manipulation du DOM (Document Object Model) avec JavaScript, couvrant la sélection d'éléments, la modification de styles, l'ajout d'événements, et l'utilisation de l'API Fetch pour les requêtes réseau.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Comment sélectionner des éléments HTML en JavaScript
- Quelles sont les différences entre les sélecteurs ID, class et tag name
- Comment modifier le style d'un élément HTML
- Comment obtenir et mettre à jour le contenu d'un élément HTML
- Comment modifier le DOM
- Comment faire une requête avec XmlHTTPRequest
- Comment faire une requête avec Fetch API
- Comment écouter/lier des événements DOM
- Comment écouter/lier des événements utilisateur

## Fichiers du projet

### Manipulation de base du DOM (0-5)
- `0-script.js` - Met la couleur du header en rouge avec `document.querySelector`
- `1-script.js` - Met la couleur du header en rouge au clic sur `#red_header`
- `2-script.js` - Ajoute la classe `red` au header au clic sur `#red_header`
- `3-script.js` - Alterne entre les classes `red` et `green` au clic sur `#toggle_header`
- `4-script.js` - Ajoute un élément `<li>` à la liste au clic sur `#add_item`
- `5-script.js` - Change le texte du header au clic sur `#update_header`

### Requêtes réseau avec Fetch API (6-8)
- `6-script.js` - Récupère et affiche un personnage Star Wars depuis l'API
- `7-script.js` - Récupère et liste tous les films Star Wars
- `8-script.js` - Récupère et affiche une traduction "hello" depuis une API

## Concepts clés

### Sélection d'éléments
```javascript
// Par tag name
document.querySelector('header');

// Par ID
document.getElementById('red_header');

// Par classe
document.querySelector('.my_list');
```

### Modification du style
```javascript
element.style.color = '#FF0000';
element.classList.add('red');
element.classList.remove('green');
element.classList.toggle('active');
```

### Modification du contenu
```javascript
element.textContent = 'New Header!!!';
element.innerHTML = '<strong>Bold text</strong>';
```

### Événements
```javascript
element.addEventListener('click', function() {
  // Code à exécuter
});
```

### Fetch API
```javascript
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => {
    // Traiter les données
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

## Exigences

- Tous les fichiers doivent se terminer par une nouvelle ligne
- Code conforme à semistandard
- Pas d'utilisation de `var`, seulement `const` et `let`
- HTML ne doit pas se recharger pour chaque action
- Tous les scripts doivent fonctionner dans Chrome (version 57.0 ou plus)

## Utilisation

### Tester les scripts

Chaque script est conçu pour fonctionner avec un fichier HTML de test correspondant :

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Test</title>
  </head>
  <body>
    <header>First HTML page</header>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
```

### Exemples d'utilisation

1. **Sélection et modification de style** (0-script.js) :
   - Sélectionne le header et change sa couleur en rouge

2. **Événements utilisateur** (1-5-script.js) :
   - Écoute les clics et modifie le DOM en conséquence

3. **Requêtes réseau** (6-8-script.js) :
   - Utilise Fetch API pour récupérer des données depuis des APIs externes

## Notes importantes

- **DOMContentLoaded** : Utilisé pour s'assurer que le DOM est chargé avant d'exécuter le script
- **Fetch API** : Méthode moderne pour faire des requêtes HTTP
- **Promises** : Les requêtes Fetch retournent des Promises, nécessitant l'utilisation de `.then()` et `.catch()`

## Auteur

Holberton School



