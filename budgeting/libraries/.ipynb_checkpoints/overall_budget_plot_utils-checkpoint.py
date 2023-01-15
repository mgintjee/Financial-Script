###############################
## Overall Budget Plot Utils                  
###############################

import expense_constants
import matplotlib.pyplot as plt
import numpy as np

def plot(networth_dict):
    sorted_year_months = list(networth_dict.keys())
    sorted_year_months.sort()
    net_list = list()
    cost_list = list()
    gain_list = list()
    # Iterate over the years
    for year_month in sorted_year_months:
        # Collect the year's dict
        year_month_budget = networth_dict[year_month]
        net_list.append(year_month_budget[expense_constants.NET_KEY])
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
    