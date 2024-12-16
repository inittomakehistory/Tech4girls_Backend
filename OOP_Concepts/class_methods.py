# Define a class BankAccount
class BankAccount:
    # Class variable
    bank_name = "Tech4Girls Bank"

    # Initialize instance variables
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    # Instance method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Current balance: ${self.balance}")

    # Instance method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")

    # Static method for bank policy
    @staticmethod
    def bank_policy():
        print("Our bank is committed to providing excellent customer service.")

    # Class method to get bank name
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name

Create instances
account1 = BankAccount("Alice")
account2 = BankAccount("Bob")

Deposit and withdraw money
account1.deposit(1000)
account1.withdraw(500)
account2.deposit(2000)
account2.withdraw(1500)

Call static and class methods
BankAccount.bank_policy()
print(BankAccount.get_bank_name())
```
