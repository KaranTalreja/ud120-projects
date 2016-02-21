#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

outlier_key = [key for key,item in data_dict.iteritems() if item['salary'] > 2.5e7 and item['salary'] != 'NaN' and item['bonus'] != 'NaN' and item['bonus'] > .8e8]
print "Outlier key",outlier_key
data_dict.pop(outlier_key[0],0)
outlier_key = [key for key,item in data_dict.iteritems() if item['salary'] > 1e6 and item['salary'] != 'NaN' and item['bonus'] != 'NaN' and item['bonus'] > 5e6]
print "Outlier key",outlier_key
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
