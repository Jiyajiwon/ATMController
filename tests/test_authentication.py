import unittest
from unittest.mock import patch
from src.authentication import authentication, insert_card

class TestAuthentication(unittest.TestCase):
    '''사용자 인증 기능 test'''

    @patch("src.utils.load_users")
    def test_authenticate_success(self, mock_laod_users):
        '''올바른 카드번호와 PIN 입력 시 인증 성공'''
        mock_laod_users.return_value = [
            {"card_number": "1234-5678-0000-0001", "pin": "0001", "restriction": False}
        ]
        user = authentication("1234-5678-0000-0001", "0001")
        self.assertIsNotNone(user)

    @patch("src.utils.load_users")
    def test_authenticate_fail(self, mock_laod_users):
        '''잘못된 카드번호와 PIN 입력 시 인증 실패'''
        mock_laod_users.return_value = [
            {"card_number": "1234-5678-0000-0001", "pin": "0001", "restriction": False}
        ]
        user = authentication("1234-5678-0000-0001", "9999")
        self.assertIsNone(user)


    @patch("builtins.input", side_effect=['1234-5678-0000-0001', "0001"])
    @patch('src.utils.load_users')
    def test_insert_card_success(self, mock_load_users, mock_input):
        mock_load_users.return_value = [
            {"card_number": "1234-5678-0000-0001", "pin": "0001", "restriction": False, "accounts": []}
        ]
        self.assertIsNotNone(insert_card())

if __name__ == "__main__":
    unittest.main()
        

    