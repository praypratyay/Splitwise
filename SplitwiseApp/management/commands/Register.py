from django.core.management import BaseCommand

from ...views import *
from ...DTOs import *

class Command(BaseCommand):
    help = 'Register User'
    
    def __init__(self):
        self.userController = UserView()
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Username')
        parser.add_argument('phoneNumber', type=int, help='Phone Number')
        parser.add_argument('email', type=str, help='Email')
        parser.add_argument('password', type=str, help='Password')

    def handle(self, *args, **kwargs):

        registerUserRequestDTO = RegisterUserRequestDTO(name=kwargs['name'], phoneNumber = kwargs['phoneNumber'], email = kwargs['email'], password = kwargs['password'])
        response = self.userController.registerUser(registerUserRequestDTO)
        print(response.status)