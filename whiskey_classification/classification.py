import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")

# print(whisky.iloc[0:10]) # capture rows
# print(whisky.iloc[0:10, 0:5]) # capture rows and columns
# print(whisky.columns)

# find flavors correlation
flavors = whisky.iloc[:, 2:14]
corr_flavors = pd.DataFrame.corr(flavors)
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()
# plt.savefig("corr_flavors.pdf")

# find whisky correlation
flavors = whisky.iloc[:, 2:14]
corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.axis("tight")
plt.colorbar()
# plt.savefig("corr_whisky.pdf")

# check from here =>
from sklearn.cluster import SpectralCoclustering
model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
print(model)

print(np.sum(model.rows_. axis=1))
print(np.sum(model.rows_. axis=0))
print(model.row_labels_)

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)
whisky = whisky.iloc[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
correlation = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())

plt.figure(figsize = (14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlation)
plt.title("Rearranged")
plt.axis("tight")
plt.savefig("correlation.pdf")
