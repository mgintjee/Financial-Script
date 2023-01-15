#####################
## File Management                
#####################

import os
import calendar
import financial_data_constants

def write_to_tsv_file(expense_tuple, tsv_file_path):
    with open(tsv_file_path, "a") as fp:
        tsv_entry = "\t".join(expense_tuple) + "\n"
        print("tsv_entry: \"" + tsv_entry + "\"")
        fp.write(tsv_entry)
        pass
    
def write_to_tsv_file_single(year, month, expense_tuple):
    if(year != "" and month != ""):
        if(len(expense_tuple) == 6):
            file_path = financial_data_constants.EXPENSES_FOLDER_PATH + year + "-" + ensure_two_characters(month) + financial_data_constants.EXPENSES_EXTENSION
            write_to_tsv_file(expense_tuple, file_path)
        else:
            print("Unable to add new entry. ExpenseTuple has an incorrect amount of elements")
    else:
        print("Unable to add new entry. Year=" + year + ", Month=" + month + " are not all valid")
            

def ensure_two_characters(integer):
    '''
    Ensures that the integer will be a 2 character string
    '''
    integer_string = str(integer)
    if(len(integer_string) == 1):
        integer_string = "0" + integer_string
    return integer_string