###########################
## Transaction Convertor                 
###########################

import transaction_convertor_constants
import type_predictor
import financial_data_constants
import history_constants
import history_utils
import datetime
import os.path

def convert():
    max_year = int(transaction_convertor_constants.MAX_YEAR)
    max_month = int(transaction_convertor_constants.MAX_MONTH)
    possible_dates = history_utils.get_possible_dates(transaction_convertor_constants.MIN_YEAR, transaction_convertor_constants.MIN_MONTH, max_year, max_month)
    possible_dates.sort(reverse=True)
    files = get_files(possible_dates)
    process_files(files)

def process_files(files):
    for file in files:
        process_file(file)
        print()

def process_file(file):
    print("#Processing file:", file)
    file_contents = file.read()
    file_parts = file_contents.split("\n")
    part_count = len(file_parts)
    for index in range(1, part_count):
        process_file_line(file.name, file_parts[index])

def process_file_line(file_name, file_line):
    if(len(file_line) > 0):
        line = file_line.replace("\"", "")
        line_parts = line.split(",")
        is_credit = transaction_convertor_constants.CREDITS_FOLDER in file_name
        print_entry(file_name, is_credit, line.split(","))
            
def print_entry(file_name, is_credit, line_parts):
    posted_date = get_date(is_credit, line_parts)
    posted_date_parts = posted_date.split("/")
    year_string = posted_date_parts[2]
    month_string = posted_date_parts[0]
    day_string = posted_date_parts[1]
    method_string = get_method(is_credit, file_name, line_parts)
    description_string = get_description(is_credit, line_parts)
    value_string = get_value(is_credit, line_parts)
    type_string = type_predictor.predict(description_string)
    if(len(value_string) != 0 and len(method_string) != 0):
        print("expense_entry_list.append((\""+year_string+"\", \""+month_string+"\", (\"" + day_string + "\", "+method_string+", \""+value_string+"\", \""+type_string+"\", (\"" + description_string+"\", \"TODO\")))")
    else:
        print("#Ignoring ", line_parts)
        
def get_files(dates):
    files = []
    for date in dates:
        file_names = get_file_names(date)
        for file_name in file_names:
            print(file_name)
            if(os.path.exists(file_name)):
                file = get_transaction_file(file_name)
                files.append(file)
    print("#Found " + str(len(files)) + " files")
    return files
    
def get_transaction_file(file_name):
    return open(file_name, "r")
    
def get_file_names(date):
    folder_string = financial_data_constants.TRANSACTIONS_FOLDER_PATH
    file_string = get_date_as_file_string(date) + "." + transaction_convertor_constants.TRANSACTION_FILE_SUFFIX
    file_names = ()
    
    for folder in transaction_convertor_constants.CHECKING_FOLDERS:
        file_names += (folder_string  + transaction_convertor_constants.CHECKINGS_FOLDER + folder + "/" + file_string,)
        
    for folder in transaction_convertor_constants.CREDITS_FOLDERS:
        file_names += (folder_string +  transaction_convertor_constants.CREDITS_FOLDER + folder + "/" + file_string,)
        
    for folder in transaction_convertor_constants.SAVINGS_FOLDERS:
        file_names += (folder_string +  transaction_convertor_constants.SAVINGS_FOLDER + folder + "/" + file_string,)
    
    return file_names
    
    
def get_date_as_file_string(date):
    year_string = str(date[history_constants.YEAR_INDEX])
    month_string = str(date[history_constants.MONTH_INDEX])
    if(len(month_string) == 1):
       month_string = "0" + month_string
    return year_string + "-" + month_string
    
def get_method(is_credit, file_name, line_parts):
    method = line_parts[transaction_convertor_constants.DESCRIPTION_INDEX]
    if(is_credit):    
        moreRewards = transaction_convertor_constants.MORE_CREDIT_FOLDER
        flagRewards = transaction_convertor_constants.FLAG_CREDIT_FOLDER
        cashRewards = transaction_convertor_constants.CASH_CREDIT_FOLDER
        if(transaction_convertor_constants.PAYMENT in method):
            return ""
        elif(moreRewards in file_name):
            return "MORE_REWARDS"
        elif(flagRewards in file_name):
            return "FLAG_REWARDS"
        elif(cashRewards in file_name):
            return "CASH_REWARDS"
        else:
            return "\"null\""
    else:
        if(transaction_convertor_constants.TRANSFER in method):
            return ""
        elif(transaction_convertor_constants.PAYMENT in method):
            return ""
        elif(transaction_convertor_constants.TRANSACTION in method):
            return ""
        elif(transaction_convertor_constants.VENMO in method):
            return transaction_convertor_constants.VENMO
        else:
            return "\"null\""
    
def get_description(is_credit, line_parts):
        return line_parts[transaction_convertor_constants.DESCRIPTION_INDEX]
    
def get_value(is_credit, line_parts):
    debit = line_parts[transaction_convertor_constants.DEBIT_INDEX]
    credit = line_parts[transaction_convertor_constants.CREDIT_INDEX]
    if(len(debit) != 0):
        return str(-int(float(debit) * 100))
    else:
        return str(int(float(credit)  * 100))
    
def get_date(is_credit, line_parts):
    if(is_credit):
        return line_parts[transaction_convertor_constants.POSTED_INDEX]
    else:
        return line_parts[transaction_convertor_constants.DATE_INDEX]
    
