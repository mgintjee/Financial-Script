#########################
## Expense Conversions                  
#########################
import math
import expense_constants
import expense_conversion_utils

def build(expense_report_dict):
    # Dict(Key: year_month_string, Value: Dict(Key: budget_type, Value: cumulative_amount))
    networth_dict = dict()
    sorted_years = list(expense_report_dict.keys())
    sorted_years.sort()
    net_amount = 0
    gain_amount = 0
    cost_amount = 0
    # Iterate over the Keys: year_string 
    for year in sorted_years:
        sorted_months = list(expense_report_dict[year].keys())
        sorted_months.sort()
        # Iterate over the Keys: month_string 
        for month in sorted_months:
            year_month = year + "-" + month
            networth_dict[year_month] = dict()
            for expense_report in expense_report_dict[year][month]:
                expense_amount = float(expense_report.get_amount()) / 100
                if(expense_amount > 0):
                    gain_amount += expense_amount
                else:
                    cost_amount += expense_amount
                net_amount += expense_amount
            networth_dict[year_month][expense_constants.NET_KEY] = net_amount
            networth_dict[year_month][expense_constants.GAIN_KEY] = gain_amount
            networth_dict[year_month][expense_constants.COST_KEY] = cost_amount
            
    return networth_dict