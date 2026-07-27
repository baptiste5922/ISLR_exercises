# Ex8 — Chapitre 2 — College.csv (ISLR)

## Résumé de la séance — exploration du dataset College.csv (ISLR)

1. **Chargement et indexation**
   - `pd.read_csv("College.csv")` : la 1ère colonne (sans nom) contient les
     noms des collèges -> pandas la nomme `Unnamed: 0`.
   - `rename(columns={'Unnamed: 0': 'College'})` : renommage EXPLICITE de
     colonne (le paramètre `columns=` est obligatoire, sinon `rename()` agit
     sur l'index par défaut).
   - `set_index('College')` : transforme cette colonne en index du
     DataFrame (équivalent à `read_csv(..., index_col=0)` en une étape).

2. **Création d'une variable catégorielle avec `pd.cut()`**
   - `college['Elite'] = pd.cut(college['Top10perc'], [0, 50, 100], labels=['No', 'Yes'])`
   - Découpe une variable continue en intervalles (bins) avec des labels.
   - Piège : les bornes doivent correspondre à l'échelle réelle de la
     donnée (ici 0-100, pas 0-1).

3. **Histogrammes et subplots**
   - `.plot.hist(bins=20, ax=...)` : nécessite `matplotlib.pyplot` (pas
     matplotlib tout court) et un axe (`ax`) explicite pour tracer
     plusieurs colonnes sur des échelles indépendantes.
   - Piège découvert : avec `subplots=True` sur un seul appel
     `.plot.hist()`, pandas calcule des bins COMMUNS à toutes les colonnes
     sélectionnées (même avec `sharex=False`) -> échelle x identique et peu
     lisible si les colonnes ont des ordres de grandeur différents.
   - Solution : un appel `.plot.hist(ax=axes[i])` séparé par colonne, sur
     des Axes créés via `plt.subplots(1, n)`.
   - `axes[i]` : les Axes retournés par `plot.hist(subplots=True)` sont
     indexables comme un array -> permet de personnaliser un subplot en
     particulier (`set_title`, `set_xlabel`, `set_ylabel`...).

4. **Taux de sélectivité (colonne calculée)**
   - `college['Accept Rate'] = college['Accept'] / college['Apps']`
   - `.nsmallest(n, col)` / `.nlargest(n, col)` : top n lignes selon une
     colonne, sans avoir à trier tout le DataFrame.
   - `.sort_values()` : sur une Series, pas besoin de préciser la colonne
     (`by=`) puisqu'il n'y en a qu'une ; sur un DataFrame, `by='colonne'`
     est obligatoire pour indiquer selon quoi trier.

5. **Agrégation par groupe**
   - `college.groupby('Elite')[['Grad.Rate', 'Outstate', 'S.F.Ratio']].agg(['mean', 'std', 'count'])`
   - `groupby()` régroupe les lignes par catégorie ; `agg()` applique
     plusieurs statistiques en une seule fois sur chaque groupe/colonne.

6. **Corrélations et heatmap manuelle**
   - `college.corr(numeric_only=True)` : matrice de corrélation carrée,
     calculée uniquement sur les colonnes numériques.
   - Piège : sélectionner une seule colonne de cette matrice
     (`corr['Grad.Rate']`) donne une Series 1D -> `plt.imshow()` plante
     (attend un tableau 2D). Utiliser la matrice complète pour `imshow()`.
   - `plt.imshow()` n'affiche que les valeurs brutes : il ignore les noms
     de lignes/colonnes du DataFrame -> il faut les ajouter à la main
     avec `plt.xticks()`/`plt.yticks()` en utilisant `corr.columns`.

Pistes à creuser plus tard : Public vs Privé (boxplot by='Private'),
détection d'outliers (Grad.Rate > 100, bug connu du dataset ISLR),
scatter Expend vs Grad.Rate.
