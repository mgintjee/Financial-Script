##########################
## Overall Budget Plots                  
##########################

import expense_conversions
import expense_plot_utils
import expense_constants
import matplotlib.pyplot as plt
import numpy as np

def plot_overall_budget(expense_report_dict):
    '''
    Plot the overall budget (Gross Income, Gross Expenses, Net Income) over time.
    '''
    # Dict(Key: year_month_string, Value: Dict(Key: budget_type, Value: cumulative_amount))
    overall_budget_dict = expense_conversions.build_overall_budget_dict(expense_report_dict)
    expense_plot_utils.plot_overall_budget(overall_budget_dict)
    