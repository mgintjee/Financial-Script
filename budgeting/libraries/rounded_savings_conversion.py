#################################
## Rounded Savings Conversions                  
#################################

import math
import expense_constants
import rounded_savings_conversion_utils

def build(expense_report_dict):
    # Dict(Key: year_string, Value: Dict(Key: month_string, Value: rounded_savings))
    rounded_savings_dict = dict()
    # Iterate over the Keys: year_string 
    for year in expense_report_dict.keys():
        # Collect the year dict
        expense_report_year_dict = expense_report_dict[year]
        # Instantiate a new dict
        rounded_savings_dict[year] = dict()
        # Iterate over the Keys: month_string 
        for month in expense_report_year_dict.keys():
            # Default the rounded savings to 0
            rounded_savings_dict[year][month] = 0
            expense_report_month_set = expense_report_year_dict[month]
            for expense_report in expense_report_month_set:
                rounded_savings_dict[year][month] += rounded_savings_conversion_utils.get_rounded_savings_from_expense(float(expense_report.get_amount()) / 100)
            
    return rounded_savings_dict