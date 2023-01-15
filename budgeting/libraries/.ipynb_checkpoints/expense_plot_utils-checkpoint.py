########################
## Expense Plot Utils                  
########################

import expense_conversion_utils
import expense_constants
import matplotlib.pyplot as plt
import numpy as np

def plot_rounded_savings(year, month_rounded_savings_dict):
    '''
    Todo
    '''
    months = list(month_rounded_savings_dict.keys())
    months.sort(reverse = True)
    rounded_savings = list(map(lambda month: abs(month_rounded_savings_dict[month]), months))
    zipped_expenses = zip(months, rounded_savings)
    # Logistics for the plt
    plt.rcdefaults()
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 5)
    # Iterate over the Y and X values
    for zipped_expense in zipped_expenses:
        plt.barh(zipped_expense[0], zipped_expense[1])
    # Iterate over the x-Values
    for i, v in enumerate(rounded_savings):
        # Display the text on the bar
        ax.text(v, i, "${:.2f}".format(v))
    # Labels and Titles
    ax.set_xlabel("Rounded Savings Amount ($)")
    ax.set_ylabel("Month")
    ax.set_title("Rounded Savings for Year=" + year)
    # Display the Plot
    plt.grid(True)
    plt.show()
    
def plot_expense_types(year, month, month_expense_types_dict):
    '''
    Todo
    '''
    expense_types = list()
    # Iterate over the expense_types
    for expense in month_expense_types_dict.items():
        if(expense[1] != 0):
            expense_types.append(expense[0])
    expense_types.sort(key=lambda expense_type: abs(month_expense_types_dict[expense_type]))
    expense_values = list(map(lambda expense_type: abs(month_expense_types_dict[expense_type]), expense_types))
    zipped_expenses = zip(expense_types, expense_values)
    # Logistics for the plt
    plt.rcdefaults()
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 5)
    # Iterate over the Y and X values
    for zipped_expense in zipped_expenses:
        color = 'red'
        if(month_expense_types_dict[zipped_expense[0]]>0):
            color = 'green'
        plt.barh(zipped_expense[0], zipped_expense[1], color=color)
    # Labels and Titles
    ax.set_xlabel("Expense Amount ($)")
    ax.set_ylabel("Expense Type")
    ax.set_title("Expense Types for Year=" + year + ", Month=" + month)
    # Display the Plot
    plt.grid(True)
    plt.show()
    
def plot_overall_budget(overall_budget_dict):
    '''
    Todo
    '''
    sorted_year_months = list(overall_budget_dict.keys())
    sorted_year_months.sort()
    net_list = list()
    cost_list = list()
    gain_list = list()
    # Iterate over the years
    for year_month in sorted_year_months:
        # Collect the year's dict
        year_month_budget = overall_budget_dict[year_month]
        net_list.append(year_month_budget[expense_constants.NET_KEY])
    print(net_list)
    # Logistics for the plt
    plt.rcdefaults()
    fig, ax = plt.subplots()
    fig.set_size_inches(15, 5)
    plt.plot(net_list)
    # Labels and Titles
    ax.set_xlabel("Year-Month")
    ax.set_ylabel("($)")
    ax.set_title("Overall Budget Over Time")
    # Ticks
    ax.set_xticks(range(0, len(sorted_year_months)))
    ax.set_xticklabels(sorted_year_months)
    plt.xticks(rotation = 45)
    # Display the Plot
    plt.grid(True)
    plt.show()
    