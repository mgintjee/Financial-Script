##########################
## Networth Plots                  
##########################

import networth_conversion
import networth_plot_utils
import expense_constants
import matplotlib.pyplot as plt
import numpy as np

def plot(expense_report_dict):
    '''
    Plot the overall budget (Gross Income, Gross Expenses, Net Income) over time.
    '''
    # Dict(Key: year_month_string, Value: Dict(Key: budget_type, Value: cumulative_amount))
    networth_dict = networth_conversion.build(expense_report_dict)
    networth_plot_utils.plot(networth_dict)
    