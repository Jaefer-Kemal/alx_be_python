# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self._account_balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
        else:
            print("Invalid deposit amount")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return True
        elif amount > self._account_balance:
            return False
        else:
            print("Invalid withdrawal amount")
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
