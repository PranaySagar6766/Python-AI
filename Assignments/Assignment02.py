from abc import  ABC, abstractmethod

class Account(ABC):
    def __init__(self , acc_id, name , balance):
        self._acc_id = acc_id
        self._name = name
        self._balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    def __str__(self):
        return f"ID: {self._acc_id} | Name: {self._name} | Balance: ₹{self._balance}"

    @property
    def acc_id(self):
        return self._acc_id

    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance

class DepositLimitReached(Exception):
    pass

class InsufficientFunds(Exception):
    pass

class InvalidAmount(Exception):
    pass

#Saving Account Class
class SavingACC(Account):
    DEPOSIT_LIMIT = 100_000
    MIN_BALANCE = 5_000
    def __init__(self, acc_id, name , balance, acc_type = 'personal'):
        super().__init__(acc_id, name,balance)
        self._acc_type = acc_type

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmount("Deposit amount must be positive.")
        if amount > self.DEPOSIT_LIMIT:
            raise DepositLimitReached(f"Cannot deposit more than ₹{self.DEPOSIT_LIMIT:,} at a time.")
        self._balance += amount
        return self._balance

    def withdraw(self ,  amount):
        if amount <= 0:
            raise InvalidAmount("Withdrawal amount must be positive.")

        if type == 'corporate':
            if amount > self._balance:
                raise InsufficientFunds(f"Insufficient Funds")

        else:
            if self._balance - amount < self.MIN_BALANCE:
                raise InsufficientFunds(f"Must maintain Min balance of ₹ {self.MIN_BALANCE}")
            self._balance -= amount
        return self._balance

#Current Account Class

class CurrentAcc(Account):
    DEPOSIT_LIMIT = 200_000
    MIN_BALANCE = 10_000
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmount("Deposit amount must be positive.")
        if amount > self.DEPOSIT_LIMIT:
            raise DepositLimitReached(f"Cannot deposit more than ₹{self.DEPOSIT_LIMIT:,} at a time.")
        self._balance += amount
        return self._balance

    def withdraw(self ,  amount):
        if amount <= 0:
            raise InvalidAmount("Withdrawal amount must be positive.")

        if type == 'corporate':
            if amount > self._balance:
                raise InsufficientFunds(f"Insufficient Funds")

        else:
            if self._balance - amount < self.MIN_BALANCE:
                raise InsufficientFunds(f"Must maintain Min balance of ₹ {self.MIN_BALANCE}")
            self._balance -= amount
        return self._balance

























    

'''from abc import ABC, abstractmethod

# ---------------- Base Class ----------------
class Account(ABC):
    def __init__(self, acc_id, name, balance):
        self._acc_id = acc_id
        self._name = name
        self._balance = balance

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    def __str__(self):
        return f"{self._acc_id}, {self._name}, Balance: {self._balance}"

    @property
    def balance(self):
        return self._balance


# ---------------- Exceptions ----------------
class DepositLimitReached(Exception):
    pass

class InsufficientFunds(Exception):
    pass


# ---------------- Savings Account ----------------
class SavingsAccount(Account):
    def __init__(self, acc_id, name, balance, acc_type="personal"):
        super().__init__(acc_id, name, balance)
        self._type = acc_type

    def deposit(self, amount):
        if amount > 100000:
            raise DepositLimitReached("You can only deposit up to 1 Lakh at a time")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if self._type == "corporate":
            # Corporate can withdraw full balance
            if amount > self._balance:
                raise InsufficientFunds("Not enough balance")
            self._balance -= amount
        else:
            # Personal must maintain min balance of 5000
            if self._balance - amount < 5000:
                raise InsufficientFunds("Minimum balance of 5000 must be maintained")
            self._balance -= amount
        return self._balance


# ---------------- Current Account ----------------
class CurrentAccount(Account):
    def deposit(self, amount):
        if amount > 200000:
            raise DepositLimitReached("You can only deposit up to 2 Lakh at a time")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if self._balance - amount < 10000:
            raise InsufficientFunds("Minimum balance of 10000 must be maintained")
        self._balance -= amount
        return self._balance


# ---------------- Transaction Class ----------------
class Transaction:
    @staticmethod
    def deposit_to_account(account: Account, amount):
        return account.deposit(amount)

    @staticmethod
    def withdraw_from_account(account: Account, amount):
        return account.withdraw(amount)


# ---------------- Bank App ----------------
def bank_app():
    # Example: create a SavingsAccount
    acc = SavingsAccount("A101", "Alice", 20000, "personal")

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            amt = int(input("Enter amount to deposit: "))
            try:
                new_balance = Transaction.deposit_to_account(acc, amt)
                print(f"Deposit successful. New balance: {new_balance}")
            except DepositLimitReached as e:
                print(e)

        elif choice == "2":
            amt = int(input("Enter amount to withdraw: "))
            try:
                new_balance = Transaction.withdraw_from_account(acc, amt)
                print(f"Withdrawal successful. New balance: {new_balance}")
            except InsufficientFunds as e:
                print(e)

        elif choice == "3":
            print(f"Final balance: {acc.balance}")
            break
        else:
            print("Invalid choice")
'''














