######################################
## Rounded Savings Conversion Utils                  
######################################
import math

def get_rounded_savings_from_expense(expense_amount):
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