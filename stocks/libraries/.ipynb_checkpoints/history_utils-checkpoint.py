##############################
## Transaction Histroy Utils                 
##############################

import datetime
import history_constants
            
def get_possible_dates(max_year, max_month):
    dates = []    
    initial_year = history_constants.INITIAL_YEAR
    for year in range(initial_year, max_year+1):
        max_months = history_constants.MONTHS_IN_YEAR
        if year == max_year:
            max_months = max_month
        for month in range(1,max_months+1):
            date = [0, 0]
            date[history_constants.YEAR_INDEX] = year
            date[history_constants.MONTH_INDEX] = month
            dates.append(date)
    
    return dates
    
def get_date_as_file_string(date):
    year_string = str(date[history_constants.YEAR_INDEX])
    month_string = str(date[history_constants.MONTH_INDEX])
    if(len(month_string) == 1):
       month_string = "0" + month_string
    return year_string + "-" + month_string

def get_max_year():
    return datetime.datetime.now().year

def get_max_month():
    return datetime.datetime.now().month