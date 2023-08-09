from ..models import *
from ..repositories import *
from ..exceptions import *
from ..strategies import TwoSetsSettleUpStrategy

class SettleUpService:

    def __init__(self):
        self.userRepository = UserRepository()
        self.groupRepository = GroupRepository()
        self.expenseRepository = ExpenseRepository()
        self.userExpenseRepository = UserExpenseRepository()
        self.twoSetsSettleUpStrategy =TwoSetsSettleUpStrategy()

    def settleUpUser(self, user_id):

        user = self.userRepository.get_user_by_id(user_id)

        if(len(user) == 0):
            raise UserDoesNotExists("User Not Found")

        # UserExpenses related to this user
        userExpenses = self.userExpenseRepository.get_userexpenses_by_user(user[0])

        expensesInvolvingUser = []
        for userExpense in userExpenses:
            expensesInvolvingUser.append(userExpense.expense)

        transactions = self.twoSetsSettleUpStrategy.settle(expensesInvolvingUser)
        filteredTransactions = []

        for transaction in transactions:

            if(transaction.from_user == user[0] or transaction.to_user == user[0]):
                filteredTransactions.append(transaction)

        return filteredTransactions
        
    def settleUpGroup(self, group_id):

        group = self.groupRepository.get_group_by_id(group_id)

        if(len(group) == 0):
            raise GroupDoesNotExists("Group Not Found")

        # UserExpenses related to this user
        groupExpenses = self.expenseRepository.get_expenses_by_group(group[0])

        transactions = self.twoSetsSettleUpStrategy.settle(groupExpenses)

        return transactions
        
