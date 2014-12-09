#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
import sys
sys.path.append("../tools/")
features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
#################################################################################

from time import time
### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

def outputKNN(n_neighbors = 5, weights = 'uniform' , algorithm = 'auto', leaf_size=30):
    from sklearn import neighbors
    
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights, algorithm, leaf_size)
    
    t0 = time()
    clf.fit(features_train,labels_train)
    print "Training Time:", round(time() - t0,3) 
    
    t0 = time()
    pred = clf.predict(features_test)
    print "Prediction Time:", round(time() - t0,3)
    
    from sklearn.metrics import accuracy_score
    
    acc = accuracy_score(labels_test, pred)
    print "K-Nearest Neighbour Accuracy: " ,acc
    prettyPicture(clf, features_test, labels_test)

def outputAdaBoost():
    from sklearn.ensemble import AdaBoostClassifier
    
    clf = AdaBoostClassifier()
    t0 = time()
    clf.fit(features_train,labels_train)
    print "Training Time:", round(time() - t0,3) 
    
    t0 = time()
    pred = clf.predict(features_test)
    print "Prediction Time:", round(time() - t0,3)
    
    from sklearn.metrics import accuracy_score
    
    acc = accuracy_score(labels_test, pred)
    print "AdaBoost Accuracy: " ,acc
    prettyPicture(clf, features_test, labels_test)

def OutputRandomForest():
    from sklearn.ensemble import RandomForestClassifier
    
    clf = RandomForestClassifier()
    t0 = time()
    clf.fit(features_train,labels_train)
    print "Training Time:", round(time() - t0,3) 
    
    t0 = time()
    pred = clf.predict(features_test)
    print "Prediction Time:", round(time() - t0,3)
    
    from sklearn.metrics import accuracy_score
    
    acc = accuracy_score(labels_test, pred)
    print "Random Forest Accuracy: " ,acc
    
    prettyPicture(clf, features_test, labels_test)
