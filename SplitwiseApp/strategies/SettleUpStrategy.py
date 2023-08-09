from abc import abstractmethod

from ..repositories import UserExpenseRepository
from ..models import UserExpenseType
from ..services import Transaction

class SettleUpStrategy:

    def settle(self):
        pass

class TwoSetsSettleUpStrategy(SettleUpStrategy):
        
        def __init__(self):
            self.userExpenseRepository = UserExpenseRepository()
    
        def settle(self, expenses):
             
            # All UserExpenses related to these expenses (involving other users)
            userExpenses = self.userExpenseRepository.get_userexpenses_by_expenses(expenses)

            # Calculating how much extra/less every user paid.
            moneyPaidExtra = {}
            for userExpense in userExpenses:
        
                user = userExpense.user
                currentExtraPaid = 0
                if(user in moneyPaidExtra):
                    currentExtraPaid = moneyPaidExtra[user]     

                if(userExpense.type == UserExpenseType.PAID):
                    moneyPaidExtra[user] = currentExtraPaid + userExpense.share
                else:
                    moneyPaidExtra[user] = currentExtraPaid - userExpense.share
                      
            extraPaid = set()
            lessPaid = set()

            for user in moneyPaidExtra:
                if(moneyPaidExtra[user] > 0):
                    extraPaid.add((user,moneyPaidExtra[user]))
                else:
                    lessPaid.add((user,moneyPaidExtra[user]))

            transactions = []

            while(len(lessPaid) != 0):
                lessPaidPair = lessPaid.pop()
                extraPaidPair = extraPaid.pop()

                transaction = Transaction()
                transaction.from_user = lessPaidPair[0]
                transaction.to_user = extraPaidPair[0]

                if(abs(lessPaidPair[1]) < extraPaidPair[1]):

                    transaction.amount_involved = abs(lessPaidPair[1])

                    if (extraPaidPair[1] - abs(lessPaidPair[1]) != 0):
                        extraPaid.add((extraPaidPair[0], extraPaidPair[1] - abs(lessPaidPair[1])))

                else:
    
                    transaction.amount_involved = extraPaidPair[1]

                    if (lessPaidPair[1] + extraPaidPair[1] != 0):
                        lessPaid.add((lessPaidPair[0], lessPaidPair[1] + extraPaidPair[1]))
                
                transactions.append(transaction)

            return transactions
        
class BruteForceSettleUpStrategy(SettleUpStrategy):
    pass
