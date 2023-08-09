from ..models import *

class UserRepository:

    def get_user_by_phoneNumber(self, phoneNumber):
        user = User.objects.filter(phoneNumber=phoneNumber)
        return user
    
    def get_user_by_id(self, user_id):
        user = User.objects.get(id=user_id)
        return user

    def save(self, user):
        user.save()

    
class GroupRepository:

    def get_group_by_id(self, group_id):
        return Group.objects.get(id=group_id)
    
    def save(self, group):
        group.save()
    
class ExpenseRepository:

    def get_expense_by_id(self, expense_id):
        return Expense.objects.get(id=expense_id)
    
    def save(self, expense):
        expense.save()
    
class UserExpenseRepository:

    def get_userexpense_by_id(self, userexpense_id):
        return UserExpense.objects.get(id=userexpense_id)