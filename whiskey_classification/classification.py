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

from sklearn.cluster.bicluster import SpectralCoclustering


# print(corr_flavors)
