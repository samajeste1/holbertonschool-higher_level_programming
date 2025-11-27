# Advanced CSS

Ce projet explore les concepts avancés du CSS, en se concentrant sur les variables CSS, les sélecteurs, les pseudo-classes, les transitions, les transformations et les animations.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer, sans l'aide de Google :

### Général
- Sélecteurs, propriétés et valeurs
- La différence entre le style block et inline
- Comment assurer la cohérence entre tous les navigateurs (CSS reset)
- Comment configurer les variables CSS
- Les différences entre CSS inline, embarqué et externe
- Comment fonctionnent les systèmes de grille (avec floats)
- La différence entre les icônes webfonts et SVG
- La différence entre les pseudo-classes et les pseudo-éléments
- Comment créer des dégradés de fond
- Comment animer des éléments en CSS
- Comment transformer (2D, 3D) des éléments
- Ce que sont les préfixes de vendeurs

## Structure du projet

Le projet est organisé en fichiers CSS progressifs qui construisent un système de design complet :

### Fichiers CSS de base (1-10)
- `1-style.css` - Comportement de défilement fluide
- `2-style.css` - Valeurs de couleur
- `3-style.css` - Variables CSS pour les couleurs
- `4-style.css` - Variables pour les polices
- `5-style.css` - Variables pour les tailles de police
- `6-style.css` - Variables pour le poids de police
- `7-style.css` - Intégration de Google Fonts
- `8-style.css` - Hauteurs de ligne
- `9-style.css` - Suppression de la décoration des liens
- `10-style.css` - Centrage des titres de section

### Fichiers CSS intermédiaires (11-20)
- `11-style.css` - Styles supplémentaires pour section-tagline
- `12-style.css` - Styles supplémentaires pour section-title
- `13-style.css` - Pseudo-classes pour les liens
- `14-style.css` - Normalisation CSS (normalize.css)
- `15-style.css` - Box-sizing universel
- `16-style.css` - Style du conteneur
- `17-style.css` - Padding des sections
- `18-style.css` - Personnalisation de la navbar
- `19-style.css` - Style de grille et variables
- `20-style.css` - Nettoyage du contexte de la grille

### Fichiers CSS avancés (21-32)
- `21-style.css` - Simplification du sélecteur col-
- `22-style.css` - Thème sombre pour les sections
- `23-style.css` - Corrections pour le thème sombre
- `24-style.css` - Arrière-plan et état hover pour services
- `25-style.css` - Bordure pour les boutons
- `26-style.css` - Border-radius pour les images
- `27-style.css` - Style de la section hero
- `28-style.css` - Correction du header et menu
- `29-style.css` - Style et propriétés personnalisées pour nav
- `30-style.css` - Correction de la section works
- `31-style.css` - Décoration de citations sur testimonials
- `32-style.css` - Incorporation de transitions

## Concepts clés

### Variables CSS (Custom Properties)
Les variables CSS permettent de stocker des valeurs réutilisables :
```css
:root {
    --color-primary: #d73953;
    --font-size-medium: 1.6rem;
}
```

### Pseudo-classes et pseudo-éléments
- **Pseudo-classes** : `:hover`, `:active`, `:visited`, `:link`
- **Pseudo-éléments** : `::before`, `::after`

### Transitions et animations
```css
transition: var(--transition-duration) var(--transition-cubic-bezier);
transform: scale(1.2);
```

### Système de grille avec floats
- Utilisation de `float: left` pour créer des colonnes
- `clear: both` pour nettoyer le contexte
- Classes `.col-1-2`, `.col-1-3` pour les colonnes

### Thème sombre
Utilisation de `[data-section-theme="dark"]` pour appliquer un thème sombre avec des variables CSS redéfinies.

## Fichiers nécessaires

### Images
Toutes les images doivent être placées dans le dossier `images/` :
- `favicon.jpg`
- `logo-black.png`
- `logo-white.png`
- `pic-about-01.jpg`
- `pic-work-01.jpg`, `pic-work-02.jpg`, `pic-work-03.jpg`
- `pic-article-01.jpg`, `pic-article-02.jpg`, `pic-article-03.jpg`
- `pic-person-01.jpg`, `pic-person-02.jpg`, `pic-person-03.jpg`

### HTML
- `index.html` - Fichier HTML principal avec la structure complète

## Exigences

- Tous les fichiers doivent se terminer par une nouvelle ligne
- Tous les fichiers doivent commencer par un commentaire décrivant la tâche
- Code conforme W3C (quand spécifié)
- Fichiers interprétés sur Chrome (version 78.x)
- Un fichier README.md à la racine du dossier du projet est obligatoire

## Utilisation

Pour visualiser le projet, ouvrez `index.html` dans un navigateur. Le fichier HTML référence `styles/32-style.css` qui contient tous les styles finaux.

Pour tester les fichiers individuels, modifiez la référence dans `index.html` :
```html
<link rel='stylesheet' href='styles/1-style.css'>
```

## Structure des fichiers CSS

Chaque fichier CSS construit sur le précédent, ajoutant progressivement :
1. Variables CSS de base
2. Styles de typographie
3. Styles de layout (grille, conteneur)
4. Styles de composants (boutons, cartes)
5. Thèmes et variations
6. Transitions et animations

## Auteur

Holberton School



