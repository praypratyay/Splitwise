from enum import Enum

class UserStatus(Enum):
    ACTIVE = 1
    INVITED = 2

class ExpenseType(Enum):
    EXPENSE = 1
    TRANSACTION = 2

class UserExpenseType(Enum):
    PAID = 1
    HADTOPAY = 2