from datetime import datetime


class Transaction:

    def __init__(self, type: str, amount: int, balance_after: int) -> str:
        self.type = type
        self.amount = amount
        self.balance_after = balance_after
        self.created_at = datetime.now()

    def __str__(self):
        time = self.created_at.strftime("%Y-%m-%d %H:%M")
        return f"{time} | {self.type} | Rs. {self.amount} | Balance: Rs. {self.balance_after}"