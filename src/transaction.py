import json

def check_balance(account):
    '''잔액 확인'''
    print(f"본 계좌의 잔액은 {account['balance']}달러입니다.")

def deposit(account):
    '''입금'''

    while True:
        deposit_amount = int(input("입금하고 싶은 금액을 숫자로 입력해주세요.: "))
        if deposit_amount < 0:
            print("유효하지 않은 금액입니다. 다시 시도하세요.")
            continue
    
        check = int(input(f"{deposit_amount} 달러를 입금하는 게 맞다면 1을, 아니면 0을 입력해주세요: "))

        if check == 1:
            break
        elif check == 0:
            continue
        else:
            print("유효하지 않은 옵션입니다. 다시 시도하세요.")

    try:
        with open('data/card_pin.json', 'r') as file:
            data = json.load(file)["users"]
        
        for user in data:
            for a in user["accounts"]:
                if a["account_number"] == account['account_number']:
                    updated_balance = a["balance"] + deposit_amount
                    a["balance"] = updated_balance

        with open('data/card_pin.json', 'w') as file:
            json.dump({"users": data}, file, indent=4)
        
        print(f"입금 후 잔액은 {updated_balance}달러입니다.")
        
    except Exception as e:
        print(e)
        return None


