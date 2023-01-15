###################
## Expense Plots                  
###################

import expense_conversions
import expense_plot_utils
import expense_constants
import matplotlib.pyplot as plt
import numpy as np

def plot_rounded_savings_over_time(expense_report_dict):
    '''
    Plot the rounded amounts for an entire month to then be transferred to a savings account.
    '''
    # Dict(Key: year_string, Value: Dict(Key: month_string, Value: rounded_savings))
    rounded_savings_dict = expense_conversions.build_rounded_savings_dict(expense_report_dict)
    sorted_years = list(rounded_savings_dict.keys())
    sorted_years.sort(reverse = True)
    # Iterate over the years
    for year in sorted_years:
        expense_plot_utils.plot_rounded_savings(year, rounded_savings_dict[year])
        
def plot_expense_types_over_time(expense_report_dict):
    '''
    Plot the different expense amounts over time.
    '''
    # Dict(Key: year_string, Value: Dict(Key: month_string, Value: Dict(Key: expense_type, Value: total_expense_amount)))
    expense_types_dict = expense_conversions.build_expense_types_dict(expense_report_dict)
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
            expense_plot_utils.plot_expense_types(year, month, year_expense_types_dict[month])
    
def plot_overall_budget(expense_report_dict):
    '''
    Plot the overall budget (Gross Income, Gross Expenses, Net Income) over time.
    '''
    # Dict(Key: year_month_string, Value: Dict(Key: budget_type, Value: cumulative_amount))
    overall_budget_dict = expense_conversions.build_overall_budget_dict(expense_report_dict)
    expense_plot_utils.plot_overall_budget(overall_budget_dict)
    
    