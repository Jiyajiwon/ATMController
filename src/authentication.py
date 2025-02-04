from src.utils import load_users, update_users_restriction

def authentication(card_number, pin):
    '''입력한 카드번호와 PIN이 일치하는지 확인'''
    users = load_users()

    for user in users:
        if user["card_number"] == card_number:
            if user['restriction'] == True:
                print("해당 카드는 ATM 이용이 제한되었습니다.")
                return None

            if user["pin"] == pin:
                return user
        
    print("카드번호 혹은 pin 번호가 일치하지 않습니다.")
    return None

def insert_card():
    '''사용자가 카드 삽입, PIN 입력'''
    print("카드를 삽입하세요.")
    card_number = input('카드번호 입력: ')

    users = load_users()
    user = None
    for u in users: 
        if u["card_number"] == card_number:
            user = u
            break

    if user is None:
        print("존재하지 않는 카드번호입니다.")
        return None
    
    if user["restriction"] == True:
        print("해당 카드는 ATM 이용이 제한되었습니다.")
        return None
    
    attempts = 0

    while attempts < 3:
        pin = input('PIN 입력: ')
        if user['pin'] == pin:
            print(f"안녕하세요, {user['name']}님.")
            return user["accounts"]
        
        attempts += 1
        print(f"인증에 실패했습니다. 앞으로 {3 - attempts} 시도 가능합니다.")

    print("3회 인증에 실패하여 ATM 이용이 제한됩니다.")
    update_users_restriction(card_number, restriction=True)
    return None
