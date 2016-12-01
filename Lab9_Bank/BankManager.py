# BankManager.py

from BankAccount import *

class BankManager(object):

    def __init__(self, bank_name):
        self.name = bank_name
        print("Creating bank:",bank_name)
        self.accounts = []

    def open_account(self,account_type, initial_deposit):
        account_number = None
        account_type = account_type.lower()
        if account_type in ["checking", "savings"]:
            account = BankAccount(account_type)
            account.deposit(initial_deposit)
            self.accounts.append(account)
            account_number = account.number
        return account_number

    def show_assets(self):
        cash = 0
        print("Current status:")
        for account in self.accounts:
            print("\tAccount number:", account.number)
            print("\t\tAccount type:", account.account_type)
            print("\t\tcurrent balance:", account.balance)
            cash += account.balance
        print("Cash on hand:", cash)

    def deposit(self, account_number, amount):
        this_account = None
        for account in self.accounts:
            if account.number == account_number:
                this_account = account
                break
        if this_account:
            this_account.deposit(amount)
        else:
            print("Illegal account number - ignored")

    def withdraw(self, account_number, amount):
        this_account = None
        for account in self.accounts:
            if account.number == account_number:
                this_account = account
                break
        if this_account:
            this_account.withdraw(amount)
        else:
            print("Illegal account number - ignored")

    def bal(self, account_number):
        this_account = None
        for account in self.accounts:
            if account.number == account_number:
                this_account = account
                break
        if this_account:
            return this_account.bal()
        else:
            print("Illegal account number - ignored")

    def setBalance(self, account_number, balance):
        this_account = None
        for account in self.accounts:
            if account.number == account_number:
                this_account = account
                break
        if this_account:
            this_account.setBalance(balance)
        else:
            print("Illegal account number - ignored")
