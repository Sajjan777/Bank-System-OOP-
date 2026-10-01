# Simple Bank

A small bank account system written in plain Python to practice object-oriented programming. It uses classes, inheritance, properties, and objects that work together. No external libraries are needed; only Python's built-in datetime module is used.

# How to run

You need Python 3 installed. Open a terminal in the project folder and run:

python main.py

# Project structure
simple-bank/
├── bank.py       # all the classes
├── main.py       # demo that shows every rule working
├── README.md
└── .gitignore

# Classes

1. Transaction

    Records one money movement: its type (deposit, withdraw, interest, transfer_in, or transfer_out), the amount, the balance after it, and the time it happened.

2. Account

    The base class for every account.

Account numbers are created automatically, starting at 1001, and never repeat.
balance is read-only, so it can only change through deposit() and withdraw().
deposit() and withdraw() return True on success and False on failure.
Failed actions don't change the balance or add a transaction.
show_history() prints every transaction for the account.
SavingsAccount (inherits from Account)
Earns interest with add_interest().
A single withdrawal can't be more than Rs. 10,000.
CurrentAccount (inherits from Account)
Can go into overdraft (a negative balance), but not below the overdraft limit.

3. Bank
    Stores accounts and finds them by account number.
    transfer() moves money between two accounts. Money is only given to the receiver if it was successfully taken from the sender.
    show_accounts() prints every account, total_balance() adds up all balances, and len(bank) gives the number of accounts.
    What the demo shows

main.py creates a bank with three accounts:

Name	Account type	Number
Sajjan	Savings (5% interest)	#1001
Sujit	Current (Rs. 5000 overdraft)	#1002
Somiyo	Basic account	#1003

It then demonstrates each rule:

A normal deposit and withdrawal, and a rejected negative deposit
A withdrawal that fails because of insufficient balance
A savings withdrawal over Rs. 10,000 being blocked
A current account going into overdraft, then being blocked past the limit
Interest being added to a savings account
A successful transfer, a transfer that fails because of low balance, and a transfer to an account that doesn't exist
Trying to set the balance directly and being stopped

Finally, it prints all accounts, the total balance, the number of accounts, and the transaction history for two accounts.