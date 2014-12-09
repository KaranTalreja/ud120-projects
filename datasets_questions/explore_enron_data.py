#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of People in the Data Set:",len(enron_data)
print "Number of features of first person:",(enron_data.keys())[0],":",len(enron_data[(enron_data.keys())[0]])
countOfPoi = 0
for key,values in dict(enron_data).iteritems():
    countOfPoi += values["poi"]
print "Featues available ",values.keys()
print "Number of POI in the data:",countOfPoi
print "Total stock value of James Prentice:",enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Number of emails from wesley colwell to POI:",enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print "Value of stock options exercised by Jeffrey Skilling:", enron_data["SKILLING JEFFREY K"]['exercised_stock_options']
