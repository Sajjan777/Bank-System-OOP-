from datetime import datetime


class Transaction:

    def __init__(self, type, amount, balance_after):
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        self.created_at = datetime.now()

    def __str__(self):
        time = self.created_at.strftime("%Y-%m-%d %H:%M")
        return f"{time} | {self.type} | Rs. {self.amount} | Balance: Rs. {self.balance_after}"


class Account:

    next_account_number = 1001

    def __init__(self, owner):
        self.account_number = Account.next_account_number
        Account.next_account_number += 1

        self.owner = owner
        self._balance = 0
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    def _add_transaction(self, transaction_type, amount):
        self.transactions.append(Transaction(transaction_type, amount, self._balance))

    def deposit(self, amount, transaction_type="deposit"):
        if amount <= 0:
            print("Error: deposit amount must be more than 0")
            return False

        self._balance += amount
        self._add_transaction(transaction_type, amount)
        return True

    def withdraw(self, amount, transaction_type="withdraw"):
        if amount <= 0:
            print("Error: withdrawal amount must be more than 0")
            return False

        if amount > self._balance:
            print("Insufficient balance")
            return False

        self._balance -= amount
        self._add_transaction(transaction_type, amount)
        return True

    def show_history(self):
        print(f"Transaction history for #{self.account_number} {self.owner}:")
        if len(self.transactions) == 0:
            print("  No transactions yet")
        for transaction in self.transactions:
            print(" ", transaction)

    def __str__(self):
        return f"#{self.account_number} {self.owner} - Balance: Rs. {self._balance}"


class SavingsAccount(Account):

    MAX_WITHDRAWAL = 10000

    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def add_interest(self):
        if self._balance <= 0:
            print("Error: no balance to add interest to")
            return False

        interest = round(self._balance * self.interest_rate, 2)
        self._balance += interest
        self._add_transaction("interest", interest)
        return True

    def withdraw(self, amount, transaction_type="withdraw"):
        if amount > SavingsAccount.MAX_WITHDRAWAL:
            print(f"Error: savings accounts can't withdraw more than Rs. {SavingsAccount.MAX_WITHDRAWAL} at once")
            return False

        return super().withdraw(amount, transaction_type)


class CurrentAccount(Account):

    def __init__(self, owner, overdraft_limit):
        super().__init__(owner)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount, transaction_type="withdraw"):
        if amount <= 0:
            print("Error: withdrawal amount must be more than 0")
            return False

        if self._balance - amount < -self.overdraft_limit:
            print(f"Error: overdraft limit of Rs. {self.overdraft_limit} reached")
            return False

        self._balance -= amount
        self._add_transaction(transaction_type, amount)
        return True


class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer(self, from_number, to_number, amount):
        sender = self.find_account(from_number)
        receiver = self.find_account(to_number)

        if sender is None or receiver is None:
            print("Transfer failed: account not found")
            return False

        if sender.withdraw(amount, "transfer_out"):
            receiver.deposit(amount, "transfer_in")
            print(f"Transferred Rs. {amount} from {from_number} to {to_number}")
            return True

        print("Transfer failed")
        return False

    def show_accounts(self):
        print(f"Accounts in {self.name}:")
        for account in self.accounts:
            print(" ", account)

    def total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

    def __len__(self):
        return len(self.accounts)

class SavingsAccount(Account):

    MAX_WITHDRAWAL = 10000

    def __init__(self, owner, interest_rate):
        super().__init__(owner)
        self.interest_rate = interest_rate

    def add_interest(self):
        if self._balance <= 0:
            print("Error: no balance to add interest to")
            return False

        interest = round(self._balance * self.interest_rate, 2)
        self._balance += interest
        self._add_transaction("interest", interest)
        return True

    def withdraw(self, amount, transaction_type="withdraw"):
        if amount > SavingsAccount.MAX_WITHDRAWAL:
            print(f"Error: savings accounts can't withdraw more than Rs. {SavingsAccount.MAX_WITHDRAWAL} at once")
            return False

        return super().withdraw(amount, transaction_type)


class CurrentAccount(Account):

    def __init__(self, owner, overdraft_limit):
        super().__init__(owner)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount, transaction_type="withdraw"):
        if amount <= 0:
            print("Error: withdrawal amount must be more than 0")
            return False

        if self._balance - amount < -self.overdraft_limit:
            print(f"Error: overdraft limit of Rs. {self.overdraft_limit} reached")
            return False

        self._balance -= amount
        self._add_transaction(transaction_type, amount)
        return True


class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer(self, from_number, to_number, amount):
        sender = self.find_account(from_number)
        receiver = self.find_account(to_number)

        if sender is None or receiver is None:
            print("Transfer failed: account not found")
            return False

        if sender.withdraw(amount, "transfer_out"):
            receiver.deposit(amount, "transfer_in")
            print(f"Transferred Rs. {amount} from {from_number} to {to_number}")
            return True

        print("Transfer failed")
        return False

    def show_accounts(self):
        print(f"Accounts in {self.name}:")
        for account in self.accounts:
            print(" ", account)

    def total_balance(self):
        total = 0
        for account in self.accounts:
            total += account.balance
        return total

    def __len__(self):
        return len(self.accounts)