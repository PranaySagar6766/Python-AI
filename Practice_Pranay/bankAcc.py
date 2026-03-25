class BankAccount:
    def __init__(self, owner , balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Amount: {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient Funds")
        elif amount > 0:
            self.__balance -= amount
            print(f"Amount Withdrawn {amount}. Remaining Balance {self.__balance}")

    def get_balance(self):
        return self.__balance


acc = BankAccount("pranay" , 100000)
acc.deposit(100000)
acc.withdraw(10000)
print("Final Balance: ", acc.get_balance())