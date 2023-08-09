from django.core.management import BaseCommand

from ...views import *
from ...DTOs import *

class Command(BaseCommand):
    help = 'SettleUp User'
    
    def __init__(self):
        self.expenseController = ExpenseView()
    
    def add_arguments(self, parser):
        parser.add_argument('-ui', '--userid', type=int, help='UserID')
        parser.add_argument('-gi', '--groupid', type=int, help='GroupID')


    def handle(self, *args, **kwargs):

        settleUpUserRequestDTO = SettleUpUserRequestDTO(user_id=kwargs['userid'])
        response = self.expenseController.settleUpUser(settleUpUserRequestDTO)
        print(response.status)