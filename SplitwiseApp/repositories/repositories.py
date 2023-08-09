from ..models import *

class UserRepository:

    def get_user_by_phoneNumber(self, phoneNumber):
        user = User.objects.filter(phoneNumber=phoneNumber)
        return user
    
    def get_user_by_id(self, user_id):
        user = User.objects.filter(id=user_id)
        return user

    def save(self, user):
        user.save()

class GroupRepository:

    def get_group_by_id(self, group_id):
        group = Group.objects.filter(id=group_id)
        return group
    
    def save(self, group):
        group.save()
    
class ExpenseRepository:

    def get_expense_by_id(self, expense_id):
        return Expense.objects.get(id=expense_id)
    
    def get_expenses_by_group(self, group):
        return Expense.objects.filter(group=group)
    
    def save(self, expense):
        expense.save()
    
class UserExpenseRepository:

    def get_userexpenses_by_user(self, user):
        userExpenses = UserExpense.objects.filter(user=user)
        return userExpenses
    
    def get_userexpenses_by_expenses(self, expenses):
        userExpenses = UserExpense.objects.filter(expense__in=expenses)
        return userExpenses