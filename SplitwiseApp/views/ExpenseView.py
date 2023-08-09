from django.views import View
from django.http import HttpResponse

from ..services import *
from ..exceptions import *
from ..DTOs import *

class ExpenseView(View): 

    def __init__(self):
        self.settleUpService = SettleUpService()

    def settleUpUser(self, request): 

        settleUpUserResponseDTO = SettleUpUserResponseDTO()
 
        try:
            transactions = self.settleUpService.settleUpUser(request.user_id)
            settleUpUserResponseDTO.transactions = transactions
            settleUpUserResponseDTO.status = "SUCCESS"

        except UserDoesNotExists as exc:
            settleUpUserResponseDTO.status = "FAILURE"
            settleUpUserResponseDTO.message = exc

        return settleUpUserResponseDTO

    def settleUpGroup(self, request): 

        settleUpGroupResponseDTO = SettleUpGroupResponseDTO()
 
        try:
            transactions = self.settleUpService.settleUpGroup(request.group_id)
            settleUpGroupResponseDTO.transactions = transactions
            settleUpGroupResponseDTO.status = "SUCCESS"

        except GroupDoesNotExists as exc:
            settleUpGroupResponseDTO.status = "FAILURE"
            settleUpGroupResponseDTO.message = exc
            
        return settleUpGroupResponseDTO
