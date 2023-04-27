from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import sklearn
import arff

# Carica il file arff
with open('tenLanguages.arff', 'r') as file:
    data = arff.load(file)

features = [row[1:] for row in data['data']]
labels = [row[0] for row in data['data']]

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2)

print("building model.")

# crea un classificatore Random Forest
clf = RandomForestClassifier()
clf = sklearn.ensemble.HistGradientBoostingClassifier()
clf = sklearn.svm.LinearSVC()

# addestra il classificatore sui dati di training
clf.fit(features_train, labels_train)

print("testing")

labels_pred = clf.predict(features_test)
acc = accuracy_score(labels_test, labels_pred)
print('Accuracy: {:.2f}%'.format(acc * 100))