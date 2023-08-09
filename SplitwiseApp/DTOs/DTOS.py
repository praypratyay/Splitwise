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