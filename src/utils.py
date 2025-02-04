import json, os


def load_users():

    try:
        with open('data/card_pin.json', 'r') as file:
            return json.load(file)["users"]
        
    except Exception as e:
        print(e)
        return None
    
def update_users_restriction(card_number, restriction = True):
    '''카드번호에 해당하는 사용자의 'restriction' 값을 업데이트'''
    try:
        with open('data/card_pin.json', 'r') as file:
            data = json.load(file)["users"]
        
        for user in data:
            if user["card_number"] == card_number:
                user["restriction"] = restriction

        with open('data/card_pin.json', 'w') as file:
            json.dump({"users": data}, file, indent=4)
        
        print("사용자는 3회 이상 인증을 실패하여 ATM 이용이 제한됩니다.")
        
    except Exception as e:
        print(e)
        return None
