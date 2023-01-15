##########################
## Rounded Savings Plot                  
##########################

import rounded_savings_conversion
import rounded_savings_plot_utils
import expense_constants
import matplotlib.pyplot as plt
import numpy as np
        
def plot(expense_report_dict):
    '''
    Plot the rounded amounts for an entire month to then be transferred to a savings account.
    '''
    # Dict(Key: year_string, Value: Dict(Key: month_string, Value: rounded_savings))
    rounded_savings_dict = rounded_savings_conversion.build(expense_report_dict)
    sorted_years = list(rounded_savings_dict.keys())
    sorted_years.sort(reverse = True)
    # Iterate over the years
    for year in sorted_years:
        rounded_savings_plot_utils.plot(year, rounded_savings_dict[year])