from django.core.management import BaseCommand

class Command(BaseCommand):
    help = 'Create Group'
    
    def add_arguments(self, parser):
        parser.add_argument('desc', type=str, help='Description of Group')
        parser.add_argument('createdBy', type=int, help='UserID of who created the group')
        parser.add_argument('-ui', '--userids', nargs='+', type=int, help='Members of the group')

    def handle(self, *args, **kwargs):
        group_desc = kwargs['desc']
        group_admin = kwargs['createdBy']
        members = kwargs['userids']

        print("-----<<<<<Group>>>>>-----")
        print(" Description : ", group_desc)
        print(" CreatedBy : ", group_admin)
        print(" Members = ", members)