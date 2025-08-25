""" The objective is to create a Python class named "Account" with methods for depositing, withdrawing, and checking balances, encapsulated in a script called "bank_account.py" to simulate basic bank account operations.

 

Create a class called "Account" that has the following attributes:

account_number (string)
account_balance (float)
account_holder (string)
The class should have the following methods:

deposit(amount: float) - This method should add the amount passed as an argument to the account balance.
withdraw(amount: float) - This method should subtract the amount passed as an argument from the account balance, but only if the account balance is greater than the amount being withdrawn.
check_balance() - This method should return the current account balance.

Instructions
 

Define the Account class and its attributes as specified above.
Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
Define the check_balance() method. It should return the current account balance.
Create an instance of the Account class, and assign it to a variable called "my_account".
Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
Test the program by creating multiple instances of the class and performing different transactions on them. """

class Account:
    def __init__(self,account_number:str,account_balance:float,account_holder:str):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self,amount:float):
        self.account_balance += amount
        print(f"The amount added is of {amount:.2f}$")

    def withdraw(self,amount:float):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.account_balance:.2f}")

        else: 
            print(f"Failed Transaction: The amount withdrew is greater than the account balance")
    
    def check_balance(self):
        return print(f"The current account is of {self.account_balance:.2f}$")
    
my_account = Account(account_number="123456789", account_holder="Alice", account_balance=100.0)

my_account.deposit(50)
my_account.withdraw(20)
my_account.check_balance()   
