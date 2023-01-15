########################
## Expense Plot Utils                  
########################

import expense_constants
import matplotlib.pyplot as plt
import numpy as np

def plot(year, month, month_expense_types_dict):
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
   