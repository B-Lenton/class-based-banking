"""
Banking App Brief:
Class-based
Withdrawal and Deposit methods
Write all transactions to a python file
Repeatedly ask the user to withdraw or deposit
"""


class BankAccount:
    
    def __init__(self, current_balance=0.00):
        self.current_balance = round(float(current_balance), 2)
        name = input("Enter your full name: ")
        self.name = name.replace(" ", "")
        self.name = self.name.replace("-", "")

    def displayBalance(self):
        print(f"Current balance: £{self.current_balance}")
    
    def withdraw(self):
        minus_amount = input("Please enter the amount you wish to withdraw: ")
        try:
            self.transaction_amount = float(minus_amount) * -1              
        except ValueError:
            self.transaction_amount = 0
        except Exception as e:
            print(f"Exception ({type(e)}): Transaction declined")
        if self.current_balance + self.transaction_amount > 0 and self.transaction_amount < 0:
            self.new_balance = self.current_balance + self.transaction_amount
            self.current_balance = self.new_balance
            return self.current_balance
        else:
            self.new_balance = self.current_balance
            print("Transaction Declined.")

    def deposit(self):
        positive_amount = input("Please enter the amount you wish to deposit: ")
        try:
            self.transaction_amount = float(positive_amount)
        except ValueError:
            self.transaction_amount = 0
        except Exception as e:
            print(f"Exception ({type(e)}): Transaction declined")
        if self.current_balance + self.transaction_amount > 0 and self.transaction_amount > 0:
            self.new_balance = self.current_balance + self.transaction_amount
            self.current_balance = self.new_balance
            return self.current_balance
        else:
            self.new_balance = self.current_balance
            print("Transaction Declined.")

    def updateBalance(self):
        self.transaction_amount = str(self.transaction_amount)
        self.new_balance = str(self.new_balance)
        bank_statement = f"{self.name}_account.txt"
        with open(bank_statement, "a") as file:
            file.write(f"Transaction: £{self.transaction_amount}\n")
            file.write(f"New balance: £{self.new_balance}\n")

banking_app = BankAccount()
banking_app.displayBalance()

while True:
    choice = input("Select 1, 2, or 3 then press Enter: 1. Withdraw, 2. Deposit, 3. Check balance\t ")

    try:
        choice = int(choice)
    except Exception:
        choice = input("Please re-enter a single number (1, 2, or 3) ")
    try:
        choice = int(choice)
    except Exception:
        print("Transaction failed.")
        quit()

    if choice == 1:
        banking_app.withdraw()
        print("\n")
        banking_app.updateBalance()
        print("\n")
        banking_app.displayBalance()
        print("\n")
    elif choice == 2:
        banking_app.deposit()
        print("\n")
        banking_app.updateBalance()
        print("\n")
        banking_app.displayBalance()
        print("\n")
    elif choice == 3:
        banking_app.displayBalance()
        print("\n")
    else:
        print("Transaction failed.\n")