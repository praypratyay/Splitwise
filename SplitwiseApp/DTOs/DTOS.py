class RegisterUserRequestDTO:
    
    def __init__(self, name, phoneNumber, email, password):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
        self.password = password

class RegisterUserResponseDTO:
    
    def __init__(self):
        self.user_id = None
        self.status = None
        self.message = None

class SettleUpUserRequestDTO:
    
    def __init__(self, user_id):
        self.user_id = user_id

class SettleUpUserResponseDTO:
    
    def __init__(self):
        self.transactions = None
        self.status = None
        self.message = None

class SettleUpGroupRequestDTO:
    
    def __init__(self, group_id):
        self.group_id = group_id

class SettleUpGroupResponseDTO:
    
    def __init__(self):
        self.transactions = None
        self.status = None
        self.message = None