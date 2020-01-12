'''
TRAINING DATA
 ____________________________________
|Weight    |  Texture  |   Label     |
|------------------------------------|
|150g      |  Bumpy    |   Orange    |
|170g      |  Bumpy    |   Orange    |
|140g      |  Smooth   |   Apple     |
|130g      |  Smooth   |   Apple     |
|...       |  ...      |   ...       |
|...       |  ...      |   ...       |
 -------------------------------------

'''

from sklearn import tree
# theFeatures = [[140, 'Smooth'], [130, 'Smooth'], [150, 'Bumpy'], [170, 'Bumpy']]
# theLabels = ['Apple', 'Apple', 'Orange', 'Orange']
theFeatures = [[140, 1], [130, 1], [150, 0], [170, 0]] # 1->Smooth, 0->Bumpy
theLabels = [0, 0, 1, 1] # 0->Apple, 1->Orange
clf = tree.DecisionTreeClassifier()
clf = clf.fit(theFeatures, theLabels)
print(clf.predict([ [150, 1] ])) #predict 150g, Smooth, and output will be 'Apple'


'''
TRAINING DATA
 ____________________________________
|HorsePower|  Seats    |   Label     |
|------------------------------------|
|300       |  2        |   sports-car|
|450       |  2        |   sports-car|
|200       |  8        |   minivan   |
|150       |  9        |   minivan   |
|...       |  ...      |   ...       |
|...       |  ...      |   ...       |
 -------------------------------------

'''