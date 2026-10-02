class Bank:

    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def find_account(self, account_number: int) -> None:
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer(self, from_number: int, to_number: int, amount: int) -> bool:
        sender = self.find_account(from_number)
        receiver = self.find_account(to_number)

        if sender is None or receiver is None:
            raise LookupError("Account not found")

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