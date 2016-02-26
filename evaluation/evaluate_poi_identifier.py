#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score, precision_score, recall_score
print "Decision tree accuracy", accuracy_score(labels_test,pred)

print "Total number of people in test set",len(pred)
print "Number of POI predicted for test set",sum(pred)

print "If predictor predicted 0 for all everyone, the accuracy is", accuracy_score(labels_test,[0]*len(pred))
print "Number of true positives in the predictions, ie. actual POI predicted", sum([1 for x,y in zip(pred,labels_test) if x == 1 and y == 1])
print "Precision score", precision_score(labels_test, pred)
print "Recall score", recall_score(labels_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] 
true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
True_positives = sum([1. for x,y in zip(predictions,true_labels) if x == 1 and y == 1])
False_positives = sum([1. for x,y in zip(predictions,true_labels) if x == 1 and y == 0])
False_negatives = sum([1. for x,y in zip(predictions,true_labels) if x == 0 and y == 1])
True_negatives = sum([1. for x,y in zip(predictions,true_labels) if x == 0 and y == 0])
print "********* Sample prediction and label set ********************"
print "True positives",sum([1 for x,y in zip(predictions,true_labels) if x == 1 and y == 1])
print "False positives",sum([1 for x,y in zip(predictions,true_labels) if x == 1 and y == 0])
print "False negatives",sum([1 for x,y in zip(predictions,true_labels) if x == 0 and y == 1])
print "True negatives",sum([1 for x,y in zip(predictions,true_labels) if x == 0 and y == 0])
# Vertical column of class in [class x class] prediction matrix
print "Precision", True_positives / (True_positives + False_positives) , " == " , precision_score(true_labels, predictions)
# Horizontal row of class in [class x class] prediction matrix
print "Recall",  True_positives / (True_positives + False_negatives) , " == ", recall_score(true_labels, predictions)
print "***************************************************************"