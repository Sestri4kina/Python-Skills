'''
In this project, I'll create a Python class that can be used to create and manipulate a personal bank account.

The bank account class you'll create should have methods for each of the following:

Accepting deposits
Allowing withdrawals
Showing the balance
Showing the details of the account
'''
class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "This account belongs to %s with current balance $%.2f" % (self.name, self.balance)
    
    def show_balance(self):
        print "The balance is $%.2f" % self.balance
        
    def deposit(self, amount):
        if amount <= 0:
            print "Error. An amount is less or equal to zero."
            return
        else:
            print "The amount depositing is $%s" % amount
            self.balance += amount
            self.show_balance()
            
    def withdraw(self, amount):
        if amount > self.balance:
            print "Not enough money on your account."
            return
        else:
            print "You withdraw $%.2f" % amount
            self.balance -= amount
            self.show_balance()
            
my_account = BankAccount("Nastia")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account

        
        