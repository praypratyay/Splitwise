from django.db import models
from django.utils import timezone

from .enums import *

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=255)
    phoneNumber = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=255)
    status = models.IntegerField(choices = UserStatus.choices, default=UserStatus.INVITED)
    #groups = models.ManyToManyField(Group) (Represented by members attribute in Group Model)


class Group(BaseModel):
    desc = models.CharField(max_length=255)
    createdBy = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Admin')
    members = models.ManyToManyField(User)


class Expense(BaseModel):
    description = models.CharField(max_length=255)
    amount = models.FloatField()
    type = models.IntegerField(choices = ExpenseType.choices, default=ExpenseType.EXPENSE)
    group = models. ForeignKey(Group, on_delete=models.PROTECT)
    createdBy = models.ForeignKey(User, on_delete=models.PROTECT)


class UserExpense(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense =  models.ForeignKey(Expense, on_delete=models.CASCADE)
    share = models.FloatField()
    type = models.IntegerField(choices = UserExpenseType.choices)
