"Modified classifier to take up to k nearest neighbors."

from scipy.spatial import distance
from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split

def euc(point_a, point_b):
    "Returns the euclidean distance between pointA and pointB."
    return distance.euclidean(point_a, point_b)

class KNNClassifier(object):
    "Classifies data up to k nearest neighbors."

    def __init__(self, k):
        self.k = k
        self.x_train = None
        self.y_train = None

    def fit(self, x_train, y_train):
        "Assigns training data and labels to class properties."
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test):
        "Predicts the label (y) for the provided data point (x)."
        predictions = []

        for row in x_test:
            label = self.closest_k(row)
            predictions.append(label)

        return predictions

    def closest_k(self, row):
        "Looks at the nearest k neighbors to predict a label."
        closest_items = {}

        # Initialize our list with the first k distances.
        for i in range(self.k):
            closest_items[euc(row, self.x_train[i])] = i

        # Keep track of the largest item in the list.
        largest = max(closest_items.keys())

        # Loop over the rest of the data, and
        # if we find a distance smaller than our largest,
        # remove the largest value and add in the new one.
        # Finally, find and set the new largest value in the list.
        # The end result will be a list with the five closest points.
        for i in range(self.k, len(self.x_train)):
            dist = euc(row, self.x_train[i])
            if dist < largest:
                closest_items.pop(largest)
                closest_items[dist] = i
                largest = max(closest_items.keys())

        # We get the labels for each of the closest items and
        # score them based on their distance.
        # The kth closest neighbor gets a score of 1/k.
        label_scores = {}
        for i, (k, v) in enumerate(closest_items.items()):
            label = self.y_train[v]
            label_scores[label] = (label_scores.get(label, 0) + (1.0 / (i + 1.0)))

        sorted_x = sorted(label_scores.items(), key=lambda i: i[1], reverse=True)

        print sorted_x
        return sorted_x[0][0]

IRIS = datasets.load_iris()
DATA = IRIS.data
TARGET = IRIS.target

X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(DATA, TARGET, test_size=.5)

MY_CLASSIFIER = KNNClassifier(5)

MY_CLASSIFIER.fit(X_TRAIN, Y_TRAIN)

PREDICTIONS = MY_CLASSIFIER.predict(X_TEST)

print accuracy_score(Y_TEST, PREDICTIONS)
