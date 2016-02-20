#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people",len(enron_data)
for key,item in enron_data.iteritems():
	print "Number of features per person", len(item.keys()), item.keys()
	break
print "Number of POI",sum([1 for key,item in enron_data.iteritems() if item["poi"] == 1])
print "Total value of the stock belonging to James Prentice", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "Email messages from Wesley Colwell to persons of interest", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "value of stock options exercised by Jeffrey Skilling",  enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]
CFO = "FASTOW ANDREW S"
CEO = "SKILLING JEFFREY K"
CHAIRMAN = "LAY KENNETH L"
for key in [CFO, CEO, CHAIRMAN]:
	print key, enron_data[key]["total_payments"] 
print "Number of quantifiable salaries",sum([1 for key,item in enron_data.iteritems() if item["salary"] != "NaN"])
print "Number of known email ids",sum([1 for key,item in enron_data.iteritems() if item["email_address"] != "NaN"])
print "Number of known people with unknown total payments",sum([1 for key,item in enron_data.iteritems() if item["total_payments"] == "NaN"])
print "Number of known POI with unknown total payments",sum([1 for key,item in enron_data.iteritems() if item["total_payments"] == "NaN" and item["poi"] == 1])
