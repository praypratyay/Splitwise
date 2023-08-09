from django.db import models

class UserStatus(models.IntegerChoices):
    ACTIVE = 1
    INVITED = 2

class ExpenseType(models.IntegerChoices):
    EXPENSE = 1
    TRANSACTION = 2

class UserExpenseType(models.IntegerChoices):
    PAID = 1
    HADTOPAY = 2