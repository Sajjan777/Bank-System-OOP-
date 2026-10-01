from account import Account, SavingsAccount, CurrentAccount
from bank import Bank


bank = Bank("Nepal Bank")

sajjan = SavingsAccount("Sajjan", 0.05)
sujit = CurrentAccount("Sujit", 5000)
somiyo = Account("Somiyo")

bank.add_account(sajjan)
bank.add_account(sujit)
bank.add_account(somiyo)

print("\n--- 1. Normal deposit and withdrawal ---")
somiyo.deposit(8000)
somiyo.withdraw(4000)
print(somiyo)

print("Trying to deposit -500:")
somiyo.deposit(-500)
print(somiyo)

print("\n--- 2. Insufficient balance ---")
somiyo.withdraw(10000)
print(somiyo)

print("\n--- 3. Savings withdrawal limit ---")
sajjan.deposit(20000)
sajjan.withdraw(15000)
sajjan.withdraw(5000)
print(sajjan)

print("\n--- 4. Current account overdraft ---")
sujit.deposit(2000)
sujit.withdraw(5000)
print(sujit)
sujit.withdraw(3000)
print(sujit)

print("\n--- 5. Adding interest ---")
sajjan.add_interest()
print(sajjan)

print("\n--- 6. Transfers ---")
bank.transfer(1001, 1003, 4000)
bank.transfer(1003, 1001, 50000)
bank.transfer(1001, 9999, 1000)

print("\n--- 7. Balance is read-only ---")
try:
    somiyo.balance = 100
except AttributeError:
    print("Can't set balance directly")

print("\n--- Summary ---")
bank.show_accounts()
print("Total balance:", bank.total_balance())
print("Number of accounts:", len(bank))

print()
sajjan.show_history()
print()
somiyo.show_history()