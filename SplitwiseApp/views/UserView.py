from django.views import View
from django.http import HttpResponse

from ..services import *
from ..exceptions import *
from ..DTOs import *

class UserView(View): 

    def __init__(self):
        self.userService = UserService()

    def registerUser(self, request): 

        registerUserResponseDTO = RegisterUserResponseDTO()

        try:
            user = self.userService.registerUser(request.name, request.phoneNumber, request.email, request.password)
            registerUserResponseDTO.user_id = user.id
            registerUserResponseDTO.status = "SUCCESS"

        except UserAlreadyExists as exc:
            registerUserResponseDTO.status = "FAILURE"
            registerUserResponseDTO.message = exc

        return registerUserResponseDTO
    