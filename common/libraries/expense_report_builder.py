############################
## Expense Report Builder                      
############################

import os
import glob
import expense_report
import sys
import os
import financial_data_constants

def build_expense_report_dict():
    expense_report_dict = dict()
    expense_report_set = build_expense_report_set()
    
    for expense_report in expense_report_set:
        expense_date = expense_report.get_date()
        expense_year = expense_date.split("-")[0]
        expense_month = expense_date.split("-")[1]
        
        if(expense_year not in expense_report_dict.keys()):
            expense_report_dict[expense_year] = dict()
            
        expense_report_year_dict = expense_report_dict[expense_year]
        
        if(expense_month not in expense_report_year_dict.keys()):
            expense_report_year_dict[expense_month] = set()
            
        expense_report_year_dict[expense_month].add(expense_report)
        
        
    return expense_report_dict

def build_expense_report_set():
    expense_files = get_all_expense_files()
    expense_report_set = set()
    for expense_file in expense_files:
        file_name = os.path.basename(expense_file)
        file_name_parts = file_name.strip(".tsv").split("-")
        year = file_name_parts[0]
        month = file_name_parts[1]
        open_file = open(expense_file, "r+")
        for file_entry in open_file:
            expense_report = build_expense_report(year, month, file_entry)
            if(expense_report is not None):
                expense_report_set.add(expense_report)                         
    return expense_report_set

def get_all_expense_files():
    extension = financial_data_constants.EXPENSES_EXTENSION
    folder_path = financial_data_constants.EXPENSES_FOLDER_PATH
    expense_files = set()
    print("Collecting *" + extension + " files from " + folder_path)
    for root, directories, file in os.walk(folder_path):
        for file in file:
            if(file.endswith(extension)) and "checkpoint" not in file:
                expense_files.add(os.path.join(root, file))
    print("Found " + str(len(expense_files)) + " *" + extension + " files to parse")
    return expense_files

def build_expense_report(year, month, tsv_entry):
    entry_parts = tsv_entry.split("\t")
    if(len(entry_parts) > 0):
        return expense_report.expense_report(year, month, entry_parts[0], entry_parts[1], entry_parts[2], entry_parts[3], entry_parts[4], entry_parts[5])
    return None