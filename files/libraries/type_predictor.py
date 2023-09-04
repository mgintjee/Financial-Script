################################
## Transaction Type Predictor                 
################################

import type_constants
import expense_types

def predict(description):    
    for expense_type in type_constants.TYPE_DICT:
        known_places = type_constants.TYPE_DICT[expense_type]
        if is_description_known(known_places, description):
            print("# Found type for description: " + str(expense_type))
            return format_expense_type(expense_type)
    print()
    print()
    print("# FIX ME!!! Unable to map this expense to a known place!!!")
    return format_expense_type(expense_types.Type.UNKNOWN)

def is_description_known(known_places, description):
    lower_case_description = description.lower()
    for known_place in known_places:
        lower_case_known_place = known_place.lower()
        if lower_case_known_place in lower_case_description:
            return True
    return False

def format_expense_type(expense_type):
    parts = str(expense_type).split(".")
    return parts[1]