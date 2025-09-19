# Exercise 4: inheritance, method overriding, encapsulation
# class BankAccount
# constructor: owner, balance
# methods: deposit, withdraw, display_balance
# class SavingAccount (inherits from BankAccount)
# constructor: owner, balance, interest_rate
# method: deposit + interest
# method: withdraw - amount + fee
# method: get_balance (overrides display_balance)
# class CurrentAccount (inherits from BankAccount)
# constructor: owner, balance, overdraft_limit

# Check overriding and encapsulation


from abc import ABC,abstractmethod

class BankAccount(ABC):
    # constructor class
    def __init__(self,owner:str,balance:float=500.0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount:float):
        if amount>0:
            self.balance+=amount
            print(f'Amount: + ${amount} has been successfully deposited to your account {self.owner}.')
        else:
            print(f'Invalid deposit amount')
    
    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f'Amount: - ${amount} has been successfully withdrawn from your account {self.owner}.')
        else:
            print(f'Insufficient Balance. Transaction failed!')

    def display_balance(self):
        print(f'Account Owner: {self.owner}')
        print(f'The current balance of the account is : ${self.balance}')

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance = 500,interest_rate=0.0):
        super().__init__(owner, balance)
        self.interest_rate=interest_rate
    #method overriding 
    def deposit(self,amount:float):
        if (amount)>0&0<(self.interest_rate)<100:
            self.balance+=(amount+(amount*((self.interest_rate)/100)))
            print(f'Amount: + ${amount} has been successfully deposited to your account {self.owner}.')
        else:
            print(f'Invalid deposit amount')
    #method overriding
    def withdraw(self,amount,fee=0):
        if 0<amount<=self.balance:
            self.balance-=amount
            if 0<=fee<amount:
                self.balance-=fee
                print(f'Amount: - ${amount} has been successfully withdrawn from your account {self.owner}.')
        else:
            print(f'Insufficient Balance. Transaction failed!')

    def get_balance(self):
        print(f'Account Owner: {self.owner}')
        print(f'The current balance of the account is : ${self.balance}')


class CurrentAccount(BankAccount):
    def __init__(self, owner, balance = 500,over_draft_limit=100):
        super().__init__(owner, balance)
        self.over_draft_limit=over_draft_limit

    def display_balance(self):
        return super().display_balance()

new_account=BankAccount('Arunesh',1000)

new_account.deposit(200)
new_account.withdraw(800)
new_account.display_balance()
print()
savings_account=SavingsAccount('Arunesh',5000,10.5)
savings_account.deposit(200)
savings_account.withdraw(8000)
savings_account.get_balance()
print()
current_account=CurrentAccount('Arunesh',3000,100)
current_account.display_balance()
