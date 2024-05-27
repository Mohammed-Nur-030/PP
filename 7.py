class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Not enough balance")

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} successfully deposited")

    def get_balance(self):
        print(f"The balance is {self.balance}")

account = BankAccount(int(input("Enter the opening balance: ")))
loop_runner = True
while loop_runner:
    print("\nBankAccount")
    print("Operations\n 1. Withdraw\n 2. Deposit\n 3. Balance\n 4. To Exit")
    option = int(input("Choice: "))
    if option == 1:
        account.withdraw(int(input("Enter the amount: ")))
    elif option == 2:
        account.deposit(int(input("Enter the amount: ")))
    elif option == 3:
        account.get_balance()
    else:
        loop_runner = False
        
