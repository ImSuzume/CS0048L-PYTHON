#encapsulation

class BankAccount:
    #constructor
    def __init__ (self, account_holder, initial_balance = 0):
        self.account_holder = account_holder
        self.__balance = initial_balance
    
    #deposit method 
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount 
            return f"Deposited {amount}. New balance is {self.__balance}. "
        return "Deposit amount must be positive "
    
    #withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount 
            return f"Withdrew {amount}. New balance is {self.__balance}. "
        return "Invalid withdrawal amount"

    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.account_holder
    

account = BankAccount ("Hadji",1000)
print (account.deposit(500))
print (account.withdraw(200))
print (account.get_balance())
print (account.account_holder)