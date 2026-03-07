from Assignment02 import Account, SavingACC, CurrentAcc, DepositLimitReached, InvalidAmount, InsufficientFunds


#Transaction Class
class Transaction:
    @staticmethod
    def deposit_to_account(account: Account, amount) -> float:
        return account.deposit(amount)

    @staticmethod
    def withdraw_from_account(account: Account, amount) -> float:
        return account.withdraw(amount)

# ---------- User / Bank App ----------
class User:
    def __init__(self, account: Account):
        self._account = account
        self._transaction_log = []

    def _log(self, action, amount, balance):
        entry = f"{action:10} | Amount: ₹{amount:>10,.2f} | Balance: ₹{balance:>10,.2f}"
        self._transaction_log.append(entry)

    def show_statement(self):
        print("\n" + "=" * 55)
        print(f"  Account Statement for: {self._account.name}")
        if not self._transaction_log:
            print("  No transactions yet.")
        for entry in self._transaction_log:
            print(" ", entry)
        print(f"  Final Balance: ₹{self._account.balance:,.2f}")

    def run(self):
        print(f"\nWelcome, {self._account.name}!")
        print(self._account)

        while True:
            print("\n--- Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                try:
                    amount = float(input("Enter amount to deposit: ₹"))
                    new_balance = Transaction.deposit_to_account(self._account, amount)
                    print(f" Deposit successful. New balance: ₹{new_balance:,.2f}")
                    self._log("DEPOSIT", amount, new_balance)
                except (DepositLimitReached, InvalidAmount) as e:
                    print(f" {e}")

            elif choice == "2":
                try:
                    amount = float(input("Enter amount to withdraw: ₹"))
                    new_balance = Transaction.withdraw_from_account(self._account, amount)
                    print(f" Withdrawal successful. New balance: ₹{new_balance:,.2f}")
                    self._log("WITHDRAWAL", amount, new_balance)
                except (InsufficientFunds, InvalidAmount) as e:
                    print(f" {e}")

            elif choice == "3":
                self.show_statement()
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

# ---------- Run ----------
if __name__ == "__main__":
    acc = SavingACC("S101", "Pranay", 20_000, acc_type="personal")
    user = User(acc)
    user.run()