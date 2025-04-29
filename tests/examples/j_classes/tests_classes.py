import unittest

from src.examples.j_classes.bank_account_db import BankAccountDB
from src.examples.j_classes.bank_account import BankAccount, get_account_object, make_deposit

class Test_Config(unittest.TestCase):

    def test_bank_account_get (self):
        
        account1 = BankAccount(500)
        self.assertEqual (account1.get_balance (), 500)

    def test_bank_account_deposit (self):

        account = BankAccount (500)
        self.assertEqual (account.get_balance (), 500)

        account.deposit (600)
        self.assertEqual (account.get_balance (), 1100)

    def test_bank_account_deposit_less_than_0 (self):

        account = BankAccount (500)
        self.assertEqual (account.get_balance (), 500)

        account.deposit (-100)
        self.assertEqual (account.get_balance (), 500)

    def test_bank_account_withdraw (self):

        account = BankAccount (500)
        self.assertEqual (account.get_balance (), 500)

        account.withdraw (400)
        self.assertEqual (account.get_balance (), 100)

    def test_bank_account_withdraw_less_than_0 (self):

        account = BankAccount (500)
        self.assertEqual (account.get_balance (), 500)

        account.withdraw (600)
        self.assertEqual (account.get_balance (), 500)

    def test_bank_account_deposit_withdraw (self):

        account = BankAccount (500)
        self.assertEqual (account.get_balance (), 500)

        account.deposit (100)
        self.assertEqual (account.get_balance (), 600)

        account.withdraw (400)
        self.assertEqual (account.get_balance (), 200)

    def test_make_deposit_free_function (self):

        account = BankAccount (500)
        self.assertEqual (account.get_balance (), 500)

        make_deposit (account)
        self.assertEqual (account.get_balance (), 600)

    def test_get_account_object (self):
        account = get_account_object ()
        print ("object", id(account))

    def test_bank_account_db_get_current_balance (self):
        db = BankAccountDB()

        self.assertEqual (True, db.get_current_balance() >= 1)
        self.assertEqual (True, db.get_current_balance() <= 10000)
