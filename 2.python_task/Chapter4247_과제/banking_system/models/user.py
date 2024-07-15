
from account import Account as acc
class User :
    def __init__(self, userName:str)->None:
        self.userName = userName
        self.account = acc()
        