from src.authentication import insert_card

def main():
    '''ATM 실행'''
    print("지원 ATM입니다.")

    # 사용자 카드 삽입 및 PIN 인증
    accounts = insert_card()
    if accounts: 
        print("계좌 목록", accounts)
    else:
        print("인증에 실패했습니다. 다시 시도하세요.")

if __name__ == "__main__":
    main()