
class BankAccount:                  # encapsulates variables and functions

    _balance = 0                    # variable PRIVATE

    def __init__(self, balance):    # constructor - assign values to class private members/ variables
        self._balance = balance

    def get_balance (self):         # functions/ methods
        return self._balance
    
    def deposit (self, amount):

        if (amount > 0):
            self._balance += amount

    def withdraw (self, amount):

        if (amount > 0 and amount <= self._balance):
            self._balance -= amount

# FREE FUNCTION (DOESN'T BELOW TO THE BANK ACCOUNT CLASS)

def make_deposit (account):
    amt = 100
    account.deposit (100)


def get_account_object ():
    account = BankAccount (50)
    print ("account object is", id(account))
    return account
