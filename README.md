# AlgoLaTeX

Ce projet permet de convertir une formule mathématique LaTeX en un arbre binaire et d'en calculer le résultat.

## Prérequis

- Python 3.12

## Utilisation

1. Exécutez le script `main.py` :
    ```bash
    python main.py
    ```

2. Entrez votre formule mathématique après etre prompté.

## Structure du Projet

- `operation.py` : Contient les fonctions pour effectuer des opérations mathématiques étape par étape.
- `main.py` : Contient la logique principale pour convertir une formule en arbre et calculer le résultat.
- `structures/` : Contient les définitions des structures de données ainsi que leurs fonctions annexes.
- `util/parseur.py` : Contient la fonction RegEx qui convertit du LaTeX au language naturel.

## Auteurs

- Hugo Dasilva Cardoso
- Amjad Ghoufrane