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