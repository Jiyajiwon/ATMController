from src.transaction import check_balance, deposit, withdraw

def select_account(user):
    '''계좌 선택'''
    print(f"{user['name']}님이 보유한 계좌 목록입니다.")
    print("===============================================")
    for idx, account in enumerate(user["accounts"], start=1):
        print(f"{idx}) 계좌: {account['account_number']}")

    try:
        index = int(input("선택을 원하는 계좌가 몇 번째인지 입력해주세요.: ")) - 1

        if index >= 0 and index < len(user["accounts"]):
            selected_account = user["accounts"][index]
            print(f"{index+1}번째 계좌인 {selected_account['account_number']}를 선택하셨습니다.")
            return selected_account
        else:
            print("유효하지 않은 입력입니다. 다시 시도하세요.")

    except Exception as e:
        print(e)
        return None
    
def select_service(account):
    '''거래 선택'''
    while True:
        print("원하시는 서비스를 선택하세요.")
        print("1) 잔액 확인")
        print("2) 입금")
        print("3) 출금")
        print("4) 종료")

        opt = int(input("이용하고 싶은 서비스의 번호를 입력해주세요.: "))

        if opt == 1:
            check_balance(account)
            print("===============================================")
        elif opt == 2:
            deposit(account)
            print("===============================================")
        elif opt == 3:
            withdraw(account)
            print("===============================================")
        elif opt == 4:
            print("거래를 종료합니다.")
            print("===============================================")
            break
        else:
            print("유효하지 않은 입력입니다. 다시 시도하세요.")
