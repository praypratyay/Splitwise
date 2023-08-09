from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Add Expense'
    
    def add_arguments(self, parser):
        parser.add_argument('desc', type=str, help='Expense Description')
        parser.add_argument('createdBy', type=int, help='UserID of who created the expense')
        parser.add_argument('amount', type=float, help='Amount Involved in expense')
        parser.add_argument('-ui', '--userids', nargs='+', type=int, help='Users Involved in Expense')
        parser.add_argument('-div', '--divisions', nargs='+', type=int, help='Divison of Amount on this expense')


    def handle(self, *args, **kwargs):
        desc = kwargs['desc']
        createdBy = kwargs['createdBy']
        amount = kwargs['amount']
        users = kwargs['userids']
        divisions = kwargs['divisions']

        print("-----<<<<<EXPENSE>>>>>-----")
        print(" Description : ", desc)
        print(" CreatedBy : ", createdBy)
        print(" Amount : ", amount)
        print(" Users Involved = ", users)
        print(" Divisions = ", divisions)

