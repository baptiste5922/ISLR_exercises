import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

college = pd.read_csv("College.csv")

college = college.rename(columns={'Unnamed: 0': 'College'})
college = college.set_index('College')

C = ['Top10perc', 'Apps', 'Enroll']

college['Elite'] = pd.cut(college['Top10perc'], [0, 50, 100], labels=['No', 'Yes'])

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

college['Outstate'].plot.hist(bins=20, ax=axes[0])
outstate = axes[0]
outstate.set_title('Répartition des établissements Outsate en fonction de tranches de prix des frais d''inscrpition')
outstate.set_xlabel('Tranches de prix en $')
outstate.set_ylabel('Nombre d''établissements')

college['Enroll'].plot.hist(bins=20, ax=axes[1])
enroll = axes[1]
enroll.set_title('Répartition du nombre d''admis en fonction du nombres d''inscription')
enroll.set_xlabel('Nb élèves admis')
enroll.set_ylabel('nb inscriptions')
#plt.show()

college['Accept Rate'] = college['Accept'] / college['Apps']
college['Accept Rate'].sort_values()

moreselect = college.nsmallest(10, 'Accept Rate')
lessselect = college.nlargest(10, 'Accept Rate')
lessselect = lessselect.sort_values(by='Accept Rate', ascending=False)

ranking_data = college.groupby('Elite')[['Grad.Rate', 'Outstate', 'S.F.Ratio']].agg(['mean', 'std', 'count'])
#print("Ranking_data")

corr = college.corr(numeric_only=True)
plt.imshow(corr)
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.colorbar()
plt.show()