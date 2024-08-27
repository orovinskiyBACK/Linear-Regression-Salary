import numpy as np
import knn_utilities as knn_utils
from collections import Counter

class KNN:
    def __init__(self, k=3):
        self.k = k

    #Training samples and training labels
    def fit(self,X, y):
        self.X_train = X
        self.y_train = y

    #Predict new samples
    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        # comput distances
        distances = [knn_utils.euclidean_distance(x, x_train) for x_train in self.X_train]

        # get k nearest samples, labels
        k_indicies = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indicies]

        # majority vote, most common class label
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]