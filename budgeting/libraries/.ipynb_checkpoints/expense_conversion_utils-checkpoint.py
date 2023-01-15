##############################
## Expense Conversion Utils                  
##############################
import math

def get_rounded_savings_from_expense(expense_amount):
    '''
    Todo
    '''
    # Default 0 as the rounded_savings
    rounded_savings = 0
    # Check that the float is negative
    if(expense_amount < 0):
        # Multiply by -1 to set it to positive
        expense_amount *= -1
        # Calculate the ceiling of the positive number
        expense_amount_rounded_up = math.ceil(expense_amount)
        # Calculate the difference of the expense_amount_rounded_up and the expense_amount
        rounded_savings = expense_amount_rounded_up - expense_amount            
    return rounded_savings

def get_expense_company_set(expense_report_dict):
    '''
    Todo
    '''
    expense_company_set = set()
    for year in expense_report_dict.keys():
        for month in expense_report_dict[year].keys():
            for expense_report in expense_report_dict[year][month]:
                expense_company_set.add(expense_report.get_company())
    return expense_company_set

def get_expense_type_set(expense_report_dict):
    '''
    Todo
    '''
    expense_type_set = set()
    for year in expense_report_dict.keys():
        for month in expense_report_dict[year].keys():
            for expense_report in expense_report_dict[year][month]:
                expense_type_set.add(expense_report.get_type())
    return expense_type_set

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