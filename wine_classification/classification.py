import numpy as np, random, scipy.stats as ss
import pandas as pd
import sklearn.preprocessing

def majority_vote_fast(votes):
    mode, count = ss.mstats.mode(votes)
    return mode

def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

def find_nearest_neighbors(p, points, k=5):
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote_fast(outcomes[ind])[0]

wine = pd.read_csv("./wine_dataset.csv", index_col=0)

wine["is_red"] = (wine["color"] == "red").astype(int)
numeric_data = wine.drop(["high_quality", "quality", "color"], axis = 1)

scaled_data = sklearn.preprocessing.scale(numeric_data)
numeric_data =  pd.DataFrame(scaled_data)

print(numeric_data.head())