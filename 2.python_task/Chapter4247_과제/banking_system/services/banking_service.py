from banking_system.models import user

us=user.User()


class BankingService:
    def __init__(self)->None:
        self.users=[]
        

    def add_user(self,userName:str)->None:
        self.users.append(us(userName))
        
    
    def find_user(self, userName:str)->user:
        try: 
            len(self.users) != 0
            for user in self.users:
                if user.userName == userName :
                    return user
        except ValueError:
            print("저장되어 있는 고객이 없습니다.")
    
    def user_menu(self, userName):
        user = self.find_user(userName)
        
        while True:
            try:
                choice = input(f"원하는 작업을 선택하세요 \n 1: 입금  2: 출금 \n 3: 잔고확인 \n 4: 거래내역 \n 5: 종료"))
                if choice == "1":
                    amount = int(input('입금할 금액을 입력하세요'))
                    user.account.diposit(amount)
                elif choice =="2":
                    amount = int(input("출금할 금액을 입력하세요"))
                    user.account.withdraw(amount)
                elif choice == "3":
                    print(f'현재 잔액은 {us.account.get_balance()} 원 입니다.')
                elif choice == "4":
                    print(f'{userName}님의 거래내역')
                    for transaction in us.account.get_transactions():
                        print(transaction)
                elif choice == "5":
                    print('종료됩니다.')
                    break
                else:
                    print('잘못된 입력번호입니다. 정확하게 입력해 주시기 바랍니다.')
                
            except ValueError as e:
                print("잘못된 입력해주세요.")
                



        
