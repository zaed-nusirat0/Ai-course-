### Challenge 1: Simple Bank Account
'''Create a `BankAccount` class that allows users to:**

1. `Deposit` an amount.
2. `Withdraw` an amount (with a check to ensure there are sufficient funds).
3. `Check balance`.

**Requirements:**

* Use private attributes to store balance information.
* Implement methods for `deposit`, `withdraw`, and `check_balance`.'''

from abc import ABC, abstractmethod

# Abstract base class for a Bank
class Bank(ABC):
    # Initializes bank balance and language with default value 'English'
    @abstractmethod
    def __init__(self, bank_balance, language='english'):
        self.bank_balance = bank_balance
        self.language = language

    # Abstract method for deposit
    @abstractmethod
    def deposit(self, amount):
        pass

    # Abstract method for withdrawal
    @abstractmethod
    def withdraw(self, amount):
        pass

    # Abstract method to check account balance
    @abstractmethod
    def check_balance_account(self):
        pass

    # Abstract method to check bank balance
    @abstractmethod
    def check_balance(self):
        pass

# Class representing the Arabic Bank, inheriting from Bank
class Arabic_Bank(Bank):
    # Welcome message
    print('Welcome to the Arab Bank'.title())
    
    # Constructor initializing bank balance, account balance, and transaction history
    def __init__(self, bank_balance, language='english'):
        super().__init__(bank_balance, language)
        self.account_balance = 0  # Balance of the client account
        self.transaction_history = []

    # Method to deposit money
    def deposit(self, amount):
        if amount <= self.bank_balance:
            # Update account and bank balance on successful deposit
            self.account_balance += amount
            self.bank_balance -= amount
            self.transaction_history.append(f"Deposit: +{amount}")
            print(f"Deposit of {amount} was successful.")
        else:
            # Insufficient funds in bank for deposit
            print(f"Deposit of {amount} failed: Insufficient bank funds.")
    
    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.account_balance:
            # Update account and bank balance on successful withdrawal
            self.account_balance -= amount
            self.bank_balance += amount
            self.transaction_history.append(f"Withdraw: -{amount}")
            print(f"Withdrawal of {amount} was successful.")
        else:
            # Insufficient funds in account for withdrawal
            print(f"Withdrawal of {amount} failed: Insufficient account balance.")

    # Method to display account balance
    def check_balance_account(self):
        print(f"Account balance: {self.account_balance}")

    # Method to display bank balance
    def check_balance(self):
        print(f"Bank balance: {self.bank_balance}")
    
    # Method to display transaction history
    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    # Method to set the preferred language
    def set_language(self, language):
        self.language = language
        print(f"Language set to {self.language}")

# Main block to run program and handle exceptions
try:
    # Request bank balance input from user
    balance = int(input('Enter the balance for bank : ').title())
    
    # Check if balance is positive to proceed
    if balance > 0:
        # Instantiate an Arabic_Bank account with the given balance
        account = Arabic_Bank(200)
        
        # Perform deposit, withdrawal, and check balances
        account.deposit(100)
        account.withdraw(50)
        account.check_balance()
        account.check_balance_account()
        
        # Show transaction history and set language to English
        account.show_transaction_history()
        account.set_language("English")
    else:
        # Insufficient initial bank balance
        print("Sorry, the amount is insufficient.".title())
except (ValueError, TypeError) as e:
    # Handle invalid or inappropriate input errors
    print(e)






