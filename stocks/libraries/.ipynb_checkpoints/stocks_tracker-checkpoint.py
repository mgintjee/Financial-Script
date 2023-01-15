####################
## Stocks Tracker           
####################

import history_utils
import history_constants
import stocks_tracker_constants
import financial_data_constants
import os.path

class stocks_tracker:
    '''
    Tracker of Stock values over time for a specific institution
    '''
    
    def __init__(self, institution_string):
        self.institution_string = institution_string
        self.date_deposits = dict()
        self.date_withdrawals = dict()
        self.date_changes = dict()
        self.date_initials = dict()
        self.date_finals = dict()
        self.dates = list()
        pass
    
    def get_institution_string(self):
        '''
        Returns the string institution name
        '''
        return self.institution_string
    
    def initialize(self):
        print("Initializing stock_tracker:", self.institution_string)
        max_year = int(history_utils.get_max_year())
        max_month = int(history_utils.get_max_month())
        possible_dates = history_utils.get_possible_dates(max_year, max_month)
        files = self.get_files(possible_dates)
        self.process_files(files)
        print("Initialized stock_tracker:", self.institution_string, "for", len(files), "months")
    
    def process_files(self, files):
        for file in files:
            self.process_file(file)
    
    def process_file(self, file):
        print("Processing file:", file)
        file_contents = file.read()
        file_parts = file_contents.split("\n")
        date_string = file_parts[stocks_tracker_constants.DATE_INDEX]
        initial_amount_string = file_parts[stocks_tracker_constants.INITIAL_INDEX]
        deposits_string = file_parts[stocks_tracker_constants.DEPOSITS_INDEX]
        withdrawals_string = file_parts[stocks_tracker_constants.WITHDRAWALS_INDEX]
        final_amount_string = file_parts[stocks_tracker_constants.FINAL_INDEX]
        self.dates.append(date_string)
        self.date_initials[date_string] = initial_amount_string
        self.date_deposits[date_string] = deposits_string
        self.date_withdrawals[date_string] = withdrawals_string
        self.date_finals[date_string] = final_amount_string

    def get_files(self, dates):
        '''
        Todo
        '''
        files = []
        for date in dates:
            file_name = self.get_file_name(date)
            if(os.path.exists(file_name)):
                file = self.get_stock_file(file_name)
                files.append(file)
        print("Found " + str(len(files)) + " historical stock files to use")
        return files
    
    def get_file_name(self, date):
        year_string = str(date[history_constants.YEAR_INDEX])
        month_string = str(date[history_constants.MONTH_INDEX])
        if(len(month_string) == 1):
           month_string = "0" + month_string
        return financial_data_constants.STOCKS_FOLDER_PATH + self.institution_string + "/" + year_string + "-" + month_string + stocks_tracker_constants.FILE_SUFFIX
    
    def get_stock_file(self, file_name):
        '''
        Todo
        '''
        return open(file_name, "r")
    
    def display(self):
        print("Displaying stock info for", self.institution_string)
        net_value_change = 0
        for date in self.dates:
            initial = float(self.date_initials[date]) / 100
            deposits = float(self.date_deposits[date]) / 100
            withdrawals = float(self.date_withdrawals[date]) / 100
            final = float(self.date_finals[date]) / 100
            value_change = round( final - initial - deposits + withdrawals, 2) 
            net_value_change += value_change 
            print(f"Date:{date:7} | Initial:{initial:10} | Deposits:{deposits:10} | Withdrawals:{withdrawals:10} | Final:{final:10} | ValueChange:{value_change:8}")
        print(f"Institution: {self.institution_string:4} | Overall return: {net_value_change:8} for {len(self.dates):3} months")