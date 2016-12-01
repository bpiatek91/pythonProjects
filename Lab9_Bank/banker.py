from BankManager import *
day = 0
def main(day):
    print("Bank Manager v1.0")
    bank = BankManager("Bank of Marble Falls")

    while True:
        choice = input("What would you like to do?")
        if choice == "n":
            day += 1
            for account in bank.accounts:
                if account.account_type in ["savings"]:
                    bank.deposit(account.number, (account.bal() * (0.04)) / 365)
            print ("Day number: ", day," of transactions")
        if choice == "c":
            account_num = bank.open_account("checking", 1000)
            print("Created account:", account_num)
        if choice == "s":
            account_num = bank.open_account("savings", 1000)
            print("Created account:", account_num)
        if choice == "d":
            aNum = int(input("What is the account number?"))
            if bank.bal(aNum) < 0:
                print("This account is locked. Your balance is:", bank.bal(aNum), "Please deposit $25")
            amount = float(input("How much would you like to deposit?"))
            if bank.bal(aNum) < 0:
                if amount >= 25:
                    bank.setBalance(aNum, 0)
                    print("Your account is unlocked! Go spend your money on drugs!")
                else:
                    print("Minimum to unlock is $25. Come back when you got the dough.")
            else:
                bank.deposit(aNum, amount)
        if choice == "w":
            aNum = int(input("What is the account number?"))
            if bank.bal(aNum) < 0:
                print("This account is locked. Your balance is:", bank.bal(aNum), "Please deposit $25")
            else:
                amount = float(input("How much would you like to withdraw?"))
                bank.withdraw(aNum, amount)
                if bank.bal(aNum) < 0:
                    bank.withdraw(aNum, 10)
        if choice == "a":
            print(bank.show_assets())
        if choice == "q":
            print("Come back soon!")
            break
main(day)
