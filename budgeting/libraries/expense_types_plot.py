###################
## Expense Plots                  
###################

import expense_types_conversion
import expense_types_plot_utils
import expense_constants
import matplotlib.pyplot as plt
import numpy as np

        
def plot(expense_report_dict):
    '''
    Plot the different expense amounts over time.
    '''
    # Dict(Key: year_string, Value: Dict(Key: month_string, Value: Dict(Key: expense_type, Value: total_expense_amount)))
    expense_types_dict = expense_types_conversion.build(expense_report_dict)
    sorted_years = list(expense_types_dict.keys())
    sorted_years.sort(reverse = True)
    # Iterate over the years
    for year in sorted_years:
        # Collect the year's dict
        year_expense_types_dict = expense_types_dict[year]
        # Sort the months
        sorted_months = list(year_expense_types_dict.keys())
        sorted_months.sort(reverse = True)
        # Iterate over the months
        for month in sorted_months:
            expense_types_plot_utils.plot(year, month, year_expense_types_dict[month])
    