
class BankAccount:
    def __init__(self, int_rate=0.01, balance=0  ):
    
        self.int_rate = int_rate 
        self.balance = balance

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
        return self 
    def withdraw(self, amount):
        
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print(" invalid amount for withdrawal")
        return self  

    def display_account_info(self):
        print(f"Balance:{self.balance}, Interest Rate: {self.int_rate * 100}")
        return self  

    def yield_interest(self):

        self.balance += self.balance * self.int_rate
        return self  

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)# added this line

user=User("Mohamad", "mohamad@mohamad.com")



Bank=BankAccount(0.03,2000)
user.account.deposit(2000)
print()

account1 = BankAccount(1, 1000)
account2 = BankAccount(2, 500)


account1.deposit(200)
account2.withdraw(100)

# selectedAccount = account1.getAccount(1)
# if selectedAccount is not None:
#     selectedAccount.deposit(200.0)
#     selectedAccount.withdraw(50.0)

# selectedAccount = account2.getAccount(2)
# if selectedAccount is not None:
#     selectedAccount.deposit(300.0)
