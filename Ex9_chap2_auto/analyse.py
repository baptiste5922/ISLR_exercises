import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix

auto = pd.read_csv("Auto.csv")

print(auto.shape)
print(auto.columns)
print(auto.head())
print(auto.isnull().sum())

auto["horsepower"] = pd.to_numeric(auto["horsepower"], errors="coerce")
print("Rows with missing horsepower:", auto["horsepower"].isna().sum())
auto = auto.dropna()

predictors = ["mpg", "cylinders", "displacement", "horsepower",
              "weight", "acceleration", "year", "origin"]

print(auto[predictors].describe())

auto2 = auto.drop(index=range(9,85))
print(auto2)


axes = scatter_matrix(auto[predictors], figsize=(15, 8), diagonal="hist",
                       alpha=0.5, s=15)
plt.suptitle("Pairwise scatterplots of Auto predictors", y=0.92)
plt.tight_layout()
plt.savefig("scatter_matrix.png", dpi=150, bbox_inches="tight")
print("Saved scatter_matrix.png")
#plt.show()

corr = auto[predictors].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, square=True)
plt.title("Corrélations entre variables numériques")
plt.tight_layout()
