class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"Balance: {self.balance}")
        print()

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient Balance")

        print(f"Balance: {self.balance}")
        print()

    def show_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")
        print()


account = BankAccount("Kavya", 0)

account.show_balance()

account.deposit(5000)

account.withdraw(2000)

account.withdraw(4000)