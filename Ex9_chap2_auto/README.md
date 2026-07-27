# Exercice 9 — Chapitre 2 (ISLR) — Dataset Auto

Analyse exploratoire du dataset `Auto.csv` (voitures, années 1970-1982).

## Contenu

- `Auto.csv` : données brutes (mpg, cylinders, displacement, horsepower, weight,
  acceleration, year, origin, name)
- `analyse.py` : script d'exploration et de visualisation
- `scatter_matrix.png` : matrice de scatterplots des prédicteurs quantitatifs

## Ce qui a été fait

1. **Nettoyage des données** : la colonne `horsepower` contenait des valeurs
   manquantes notées `"?"`, ce qui forçait pandas à la lire comme du texte.
   Conversion en numérique (`pd.to_numeric(..., errors="coerce")`) puis
   suppression des lignes concernées (5 lignes sur 397).

2. **Statistiques descriptives** : calcul de la moyenne, de l'écart-type et
   du range (min/max) pour chaque prédicteur quantitatif, sur l'ensemble du
   dataset puis sur un sous-ensemble (suppression des observations 10 à 85).

3. **Matrice de scatterplots** (`scatter_matrix`) des prédicteurs quantitatifs
   entre eux, pour visualiser les relations deux à deux.

4. **Heatmap de corrélation** (seaborn) sur la même matrice de corrélation,
   pour visualiser plus rapidement l'intensité des relations linéaires.

## Principaux constats

- `mpg` est fortement corrélée négativement à `displacement`, `horsepower` et
  `weight` (relation non linéaire, en forme de courbe décroissante) : plus
  une voiture est grosse/puissante, moins elle est économe en carburant.
- `displacement`, `horsepower`, `weight` et `cylinders` sont très corrélées
  entre elles (colinéarité) — attendu, car un plus gros moteur implique plus
  de cylindres, plus de puissance et une voiture plus lourde.
- `acceleration` est corrélée négativement avec la puissance/le poids et
  positivement avec `mpg` : les voitures lourdes et puissantes accélèrent
  plus lentement (0-60).
- `year` est légèrement corrélée positivement avec `mpg`, reflétant
  l'amélioration progressive de l'efficacité énergétique après le choc
  pétrolier des années 70.
- `origin` (1 = USA, 2 = Europe, 3 = Japon) est associée aux autres
  prédicteurs : les voitures américaines du dataset sont en moyenne plus
  lourdes, plus puissantes et moins économes que les européennes/japonaises.
