import unittest
from unittest.mock import patch
from src.atm import select_account, select_service

class TestATM(unittest.TestCase):
    '''계좌 선택과 거래 선택 기능 test'''

    @patch("builtins.input", side_effect=["1"])
    def test_select_account(self, mock_input):
        """올바른 계좌 선택 시 해당 계좌 return"""
        test_user = {
            "name": "Jiwon Ryu",
            "card_number": "1234-5678-9876-5432",
            "accounts": [
                {"account_number": "1001001", "balance": 500000},
                {"account_number": "1001002", "balance": 250000}
            ]
        }
        selected_account = select_account(test_user)
        self.assertEqual(selected_account["account_number"], "1001001")

    @patch("builtins.input", side_effect=["4"])
    def test_select_service_exit(self, mock_input):
        """사용자가 4. 종료 선택 시 서비스 종료"""
        test_account = {"account_number": "1001001", "balance": 500000}
        self.assertIsNone(select_service(test_account))

if __name__ == "__main__":
    unittest.main()
