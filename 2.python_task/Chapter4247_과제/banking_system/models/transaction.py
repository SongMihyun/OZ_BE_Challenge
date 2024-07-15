class Transaction:                          #거래(Transaction) 클래스 정의
    def __init__(self,transaction_type:str,amount:int,balance:int)->None:
        self.transaction_type=transaction_type          # "입금","출금" 거래 유형을 나타내는 문자열
        self.amount=amount                              # 거래 금액을 나타내는 정수
        self.balance = balance                    # 거래후 잔고를 나타내는 정수
        
    def __str__(self) -> str:
        return f'[{self.transaction_type}] 금액 : {self.amount}원 \n 거래후 잔액: {self.__balance}원'
    
    def to_tuple(self):
        transcation_tuple=self.transaction_type,self.amount,self.__balance
        return transcation_tuple
    
