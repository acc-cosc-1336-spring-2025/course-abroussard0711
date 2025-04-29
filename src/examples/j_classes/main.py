
from bank_account import BankAccount
from bank_account_db import BankAccountDB
from atm import ATM, run_menu

def main ():
    
#    account = BankAccount(500)              # variable represent a BankAccount --- object or instance of a class
#    print (account.get_balance())
#
#    amount = input ('Enter amount to deposit: ')
#    account.deposit (int(amount))
#    print (account.get_balance ())
#
#    amount = input ('Enter amount to withdraw: ')
#    account.withdraw (int(amount))
#    print (account.get_balance ())

    bankAccountDB = BankAccountDB()
    
    account1 = BankAccount(bankAccountDB.get_current_balance ())     #variable represents a BankAccount--- object or instance of a class
    atm = ATM (account1)

#    atm.display_balance()
#    atm.make_deposit()
#    atm.make_withdraw()

#    atm.display_balance()
#    print(account1.get_balance())

    run_menu (atm)

    print (account1.get_balance ())

main ()