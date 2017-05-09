from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)

class ScrappyKNN():
    def __init__(self, k):
        self.k = k

    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
    

    def predict(self, x_test):
        predictions = []

        for row in x_test:
            label = self.closestK(row)
            predictions.append(label)

        return predictions

    def closestK(self, row):
        items = {}
        
        for i in range(self.k):
            items[euc(row, self.x_train[i])] = i

        largest = max(items.keys())
        
        for i in range(self.k, len(self.x_train)):
            dist = euc(row, self.x_train[i])
            if dist < largest:
                items.pop(largest)
                items[dist] = i
                largest = max(items.keys())
        
        labelCounts = {}
        for i, j in items.items():
            label = self.y_train[j]
            labelCounts[label] = labelCounts.get(label, 0) + 1
        
        x = sorted(labelCounts.items(), key=lambda i:i[1])

        return x[0][0]


        
        

from sklearn import datasets
iris = datasets.load_iris()

x = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .5)

#from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN(5)

my_classifier.fit(x_train, y_train)

predictions = my_classifier.predict(x_test)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)