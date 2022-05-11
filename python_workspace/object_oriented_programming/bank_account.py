class BankAccount():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('Amount deposited')

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            print('Amount Withdrawn')
        else:
            print('Funds Unavailable!')

    def __str__(self):
        return 'Account owned by {} has balance Rs.{}'.format(self.owner, self.balance)


account = BankAccount("Vijay", 1000)
print(str(account))
account.deposit(200)
print(str(account))
account.withdraw(700)
print(str(account))
account.withdraw(500)
print(str(account))
account.withdraw(1)
print(str(account))
