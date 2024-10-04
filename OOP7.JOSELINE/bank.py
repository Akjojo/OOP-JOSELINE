class BankAccount:
    interest_rate = 0.05  # class variable

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance:.2f}")

        # Create two instances of BankAccount
account1 = BankAccount("John Doe")
account2 = BankAccount("Jane Smith")

#deposits and withdrawals
account1.deposit(1000)
account1.withdraw(500)
account2.deposit(2000)
account2.withdraw(800)

#interest
account1.apply_interest()
account2.apply_interest()

# Display account information for each account
print("Account 1:")
account1.display_account_info()
print("\nAccount 2:")
account2.display_account_info()