#########################
## Expense Conversions                  
#########################
import math
import expense_constants
import expense_conversion_utils

def build_rounded_savings_dict(expense_report_dict):
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
                rounded_savings_dict[year][month] += expense_conversion_utils.get_rounded_savings_from_expense(float(expense_report.get_amount()))
            
    return rounded_savings_dict
    
def build_expense_types_dict(expense_report_dict):
    # Dict(Key: year_string, Value: Dict(Key: month_string, Value: Dict(Key: expense_type Value: total_expense_amount)))
    expense_types_dict = dict()
    expense_type_set = expense_conversion_utils.get_expense_type_set(expense_report_dict)
    sorted_years = list(expense_report_dict.keys())
    sorted_years.sort()
    total_expense = "TotalExpense"
    # Iterate over the Keys: year_string 
    for year in sorted_years:
        sorted_months = list(expense_report_dict[year].keys())
        sorted_months.sort()
        expense_types_dict[year] = dict()
        # Iterate over the Keys: month_string 
        for month in sorted_months:
            expense_types_dict[year][month] = dict()
            for expense_report in expense_report_dict[year][month]:
                if len(expense_types_dict[year][month]) == 0:
                    for expense_type in expense_type_set:
                        expense_types_dict[year][month][expense_type] = 0
                        expense_types_dict[year][month][total_expense] = 0
                expense_types_dict[year][month][expense_report.get_type()] += float(expense_report.get_amount())
                if float(expense_report.get_amount()) < 0:
                    expense_types_dict[year][month][total_expense] += float(expense_report.get_amount())
                    
    return expense_types_dict

def build_overall_budget_dict(expense_report_dict):
    # Dict(Key: year_month_string, Value: Dict(Key: budget_type, Value: cumulative_amount))
    overall_budget_dict = dict()
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
            overall_budget_dict[year_month] = dict()
            for expense_report in expense_report_dict[year][month]:
                expense_amount = float(expense_report.get_amount())
                if(expense_amount > 0):
                    gain_amount += expense_amount
                else:
                    cost_amount += expense_amount
                net_amount += expense_amount
            overall_budget_dict[year_month][expense_constants.NET_KEY] = net_amount
            overall_budget_dict[year_month][expense_constants.GAIN_KEY] = gain_amount
            overall_budget_dict[year_month][expense_constants.COST_KEY] = cost_amount
            
    return overall_budget_dict

def build_gross_expense_types_dict(expense_report_dict):
    '''
    Todo
    '''
    # Collect the possible expense types
    expense_type_set = get_expense_type_set(expense_report_dict)
    # Dict(Key: year_string, Value: Dict(Key: month_string, Value: Dict(Key: gross_type Value: total_gross_amount)))
    gross_expenses_dict = dict()
    sorted_years = list(expense_report_dict.keys())
    index_dict = dict()
    # Dict(Key: year_index, Value: year_string)
    year_index_dict = dict()
    # Dict(Key: year_index, Value: Dict(Key: month_index, Value: month_string))
    month_index_dict = dict()
    sorted_years.sort()
    year_index = 0
    # Iterate over the Keys: year_string 
    for year in sorted_years:
        # Set the year_index and year
        year_index_dict[year_index] = year
        # Default an empty dict for this year's months
        month_index_dict[year_index] = dict()
        sorted_months = list(expense_report_dict[year].keys())
        sorted_months.sort()
            # Default an empty dictionary for this year
        gross_expenses_dict[year] = dict()
        month_index = 0
        # Iterate over the Keys: month_string 
        for month in sorted_months:
            # Set the month_index and month
            month_index_dict[year_index][month_index] = month
            # Default an empty dictionary for this month
            gross_expenses_dict[year][month] = dict()
            
            # Check if there are previous values to start at
            if(year_index != 0 or month_index != 0):
                prev_year_index = year_index
                prev_month_index = month_index
                
                # Check to see if the previous month is the first for the year
                if(month_index == 0):
                    prev_year_index -= 1
                    prev_month_index = len(gross_expenses_dict[year_index_dict[prev_year_index]])-1
                # Otherwise use the previous month
                else:
                    prev_month_index -= 1
                prev_year = year_index_dict[prev_year_index]
                prev_month = month_index_dict[prev_year_index][prev_month_index]
                # Populate with the default values
                for expense_type in expense_type_set:
                    gross_expenses_dict[year][month][expense_type] = gross_expenses_dict[prev_year][prev_month][expense_type]
                
            # Otherwise this is the first dict to input
            else:
                # Populate with the default values
                for expense_type in expense_type_set:
                    gross_expenses_dict[year][month][expense_type] = 0
            # Iterate over the expense_reports
            for expense_report in expense_report_dict[year][month]:
                gross_expenses_dict[year][month][expense_report.get_type()] += float(expense_report.get_amount())
            month_index += 1
        year_index += 1
    return gross_expenses_dict