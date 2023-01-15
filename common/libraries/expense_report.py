####################
## Expense Report                    
####################

class expense_report:
    '''
    Expense Report object that aggregates the information pertaining to a single expense in a single object
    '''
    
    def __init__(self, expense_year, expense_month, expense_day, expense_method, expense_amount, expense_type, expense_company, expense_reason):
        '''
        Construct the expense report with the following parameters:
        expense_year: string year in YYYY format
        expense_month: string month in MM format
        expense_day: string day in DD format
        expense_method: string method of payment
        expense_amount: string amount in dollars
        expense_type: string type 
        expense_company: string company
        expense_reason: string reason
        '''
        self.expense_year = expense_year
        self.expense_month = expense_month
        self.expense_day = expense_day
        self.expense_method = expense_method
        self.expense_amount = expense_amount
        self.expense_type = expense_type
        self.expense_company = expense_company
        self.expense_reason = expense_reason
        pass
    
    def get_date(self):
        '''
        Returns the string date of this expense in YYYY/MM/DD format
        '''
        return self.expense_year + "-" + self.expense_month + "-" + self.expense_day
    
    def get_method(self):
        '''
        Returns the string method of payment for this expense
        '''
        return self.expense_method
    
    def get_type(self):
        '''
        Returns the string type of this expense
        '''
        return self.expense_type
    
    
    def get_amount(self):
        '''
        Returns the string dollar amount of the this expense
        '''
        return self.expense_amount
    
    def get_company(self):
        '''
        Return the string name of the company this expense was at 
        '''
        return self.expense_company
    
    def get_reason(self):
        '''
        Return the string reason for this expense. From people to items
        '''
        return self.expense_reason
    
    def to_string(self):
        '''
        Return the string representation of this expense_report
        '''
        to_string = "expense_report"
        to_string += "\n> date=" + self.get_date()
        to_string += "\n> method=" + self.expense_method
        to_string += "\n> type=" + self.expense_type
        to_string += "\n> amount=" + self.expense_amount
        to_string += "\n> company=" + self.expense_company
        to_string += "\n> reason=" + self.expense_reason
        return to_string