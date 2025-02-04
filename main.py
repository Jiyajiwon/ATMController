from src.authentication import insert_card
from src.atm import select_account

def main():
    '''ATM 실행'''
    print("지원 ATM입니다.")

    # 사용자 카드 삽입 및 PIN 인증
    user = insert_card()
    if user is None:
        print("인증에 실패했습니다. 다시 시도하세요.")
        return None

    selected_account = select_account(user)
    if not selected_account:
        print("해당하는 계좌가 없습니다. 다시 시도하세요.")
        return None


if __name__ == "__main__":
    main()