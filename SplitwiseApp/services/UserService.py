from ..models import *
from ..repositories import *
from ..exceptions import *

class UserService:

    def __init__(self):
        self.userRepository = UserRepository()

    def registerUser(self, name, phoneNumber, email, password):

        user = self.userRepository.get_user_by_phoneNumber(phoneNumber)

        if(len(user) != 0):

            if (user[0].status == UserStatus.ACTIVE):
                raise UserAlreadyExists("ACTIVE User Exists")
            else:
                user[0].status = UserStatus.ACTIVE
                user[0].name = name
                user[0].phoneNumber = phoneNumber
                user[0].email = email
                user[0].password = password
                self.userRepository.save(user[0])
                return user[0]  
        else:
                user = User()
                user.status = UserStatus.ACTIVE
                user.name = name
                user.phoneNumber = phoneNumber
                user.email = email
                user.password = password
                self.userRepository.save(user)
                return user
        
            