############################
## Expense Type Constants                 
############################

from enum import Enum

class Type(Enum):
    UNKNOWN = -1
    INCOME = 0
    REWARD = 1
    DIVIDEND = 2
    COMPENSATION = 3
    MATERIALISM = 4
    GROCERIES = 5
    RESTAURANT = 6
    ENTERTAINMENT = 7
    CAR_EXPENSES = 8
    PET_EXPENSES = 9
    HEALTHCARE = 10
    FEE = 11
    POLITICS = 12
    HOUSING = 13
    TRAVEL = 14
    MISC = 15