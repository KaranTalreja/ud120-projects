#!/usr/bin/python

import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    dtype = [('predictions',float), ('ages',float), ('net_worths',float),('residual_error',float)]
    residual = (np.array(predictions) - np.array(net_worths))**2
    values = zip(predictions,ages,net_worths,residual)
    array = np.array(values,dtype=dtype)
    sorted_array = np.sort(array,kind='mergesort',order="residual_error")
    cleaned_data = sorted_array[:-len(sorted_array)*0.1][["ages","net_worths","residual_error"]]
    print "Cleaning of outliers"
    return cleaned_data

