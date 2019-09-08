from sklearn import tree
X = [[80, 185], [50, 155], [87, 178], [65, 170], [68, 169]]

Y = ['male', 'male', 'female', 'female', 'male']

classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(X, Y)

prediction = classifier.predict([[75, 170]])

print(prediction)