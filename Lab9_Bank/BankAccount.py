# BankAccount.py - manage accounts

class BankAccount(object):

    ACCOUNT_NUMBER = 1000

    def __init__(self, account_type):
        self.account_type = account_type
        self.number = BankAccount.ACCOUNT_NUMBER
        BankAccount.ACCOUNT_NUMBER += 1
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def bal(self):
        return self.balance

    def setBalance(self, num):
        self.balance = num
