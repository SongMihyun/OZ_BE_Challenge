from transaction import Transaction

trans = Transaction()



class Account:
    bank_name = "MyBank"
    
    def __init__(self):
        self.transitons = []
        self.__balance = 1000
        
    
    def diposit(self, amount: int)->None:
        try :
            amount > 0
            self.__balance += amount
            self.transitons.append(trans("입금",amount,self.__balance))
        except ValueError:
            print("입력한 숫자가 유효하지 않습니다. 다시 입력해 주세요.")
    
    def withdraw(self, amount: int)->None:
        try:
            amount >= self.__balance
            self.__balance -= amount
            self.transitons.append(trans("출금",amount,self.__balance))
        except ValueError:
            print(f"잔액이 모자랍니다.")
    
    def get_balance(self) -> int:
        return self.__balance
    
    def get_transactions(self)->list:
        return self.transitons
        
        
    def get_bank_name(cls)->str:
        return cls.bank_name
        

    def set_bank_name(cls,name:str)->None:
        cls.bank_name = name
        
    





