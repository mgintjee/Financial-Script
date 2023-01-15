########################
## Expense Plot Utils                  
########################

import matplotlib.pyplot as plt
import numpy as np

def plot(year, month_rounded_savings_dict):
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