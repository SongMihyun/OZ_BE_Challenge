
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from banking_system.services.banking_service import BankingService

def main() -> None:
    system = BankingService()
    while True:
        try:
            choice = input("1: 사용자 추가, 2: 사용자 찾기, 3: 종료: ")
            if choice == '1':
                username = input("사용자 이름을 입력하세요: ")
                system.add_user(username)
            elif choice == '2':
                username = input("사용자 이름을 입력하세요: ")
                system.user_menu(username)
            elif choice == '3':
                break
            else:
                print("잘못된 입력입니다. 다시 시도하세요.")
        except ValueError as e:
            print(f"잘못된 입력입니다: {e}")
    
if __name__ == "__main__":
    main()