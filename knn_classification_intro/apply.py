import classification as cls
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris = datasets.load_iris()
predictors = iris.data[:, 0:2]
outcomes = iris.target

plt.plot(predictors[outcomes==0][:,0], predictors[outcomes==0][:,1], "ro")
plt.plot(predictors[outcomes==1][:,0], predictors[outcomes==1][:,1], "go")
plt.plot(predictors[outcomes==2][:,0], predictors[outcomes==2][:,1], "bo")
# plt.savefig("iris.pdf")

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)

my_predictions = np.array([cls.knn_predict(p, predictors, outcomes, 5) for p in predictors])

print(sk_predictions.shape)
print(my_predictions.shape)
print(100*np.mean(sk_predictions == my_predictions))
print(100*np.mean(sk_predictions == outcomes))
print(100*np.mean(sk_predictions == outcomes))

print(iris.data[:, 0:])
# k = 5; filename = "iris_grid.pdf"; limits = (4.8,8,1.5,4); h = 0.1
# (xx, yy, prediction_grid) = cls.make_prediction_grid(predictors, outcomes, limits, h, k)
# cls.plot_prediction_grid(xx, yy, prediction_grid, filename, predictors, outcomes)
