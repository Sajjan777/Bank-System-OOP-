from account import Account, SavingsAccount, CurrentAccount
from bank import Bank


def ask_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


bank = Bank("NIC ASIA Bank")

while True:
    print("\n---- NIC ASI Bank ----")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Add interest")
    print("6. Transaction history")
    print("7. Show all accounts")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("1. Basic  2. Savings  3. Current")
        account_type = input("Choose type: ")
        name = input("Owner name: ")

        if account_type == "1":
            account = Account(name)
        elif account_type == "2":
            rate = ask_number("Interest rate in %: ")
            account = SavingsAccount(name, rate / 100)
        elif account_type == "3":
            limit = ask_number("Overdraft limit: ")
            account = CurrentAccount(name, limit)
        else:
            print("Invalid type")
            continue

        bank.add_account(account)
        print("Account created! Account number:", account.account_number)

    elif choice == "2":
        number = int(ask_number("Account number: "))
        account = bank.find_account(number)
        if account is None:
            print("Account not found")
        else:
            amount = ask_number("Amount to deposit: ")
            account.deposit(amount)
            print(account)

    elif choice == "3":
        number = int(ask_number("Account number: "))
        account = bank.find_account(number)
        if account is None:
            print("Account not found")
        else:
            amount = ask_number("Amount to withdraw: ")
            try:
                account.withdraw(amount)
                print(account)
            except ValueError as e:
                print("Error:", e)

    elif choice == "4":
        sender = int(ask_number("From account number: "))
        receiver = int(ask_number("To account number: "))
        amount = ask_number("Amount to transfer: ")
        bank.transfer(sender, receiver, amount)

    elif choice == "5":
        number = int(ask_number("Savings account number: "))
        account = bank.find_account(number)
        if isinstance(account, SavingsAccount):
            time = ask_number("Time in years: ")
            account.add_interest(time)
            print(account)
        else:
            print("Not a savings account")

    elif choice == "6":
        number = int(ask_number("Account number: "))
        account = bank.find_account(number)
        if account is None:
            print("Account not found")
        else:
            account.show_history()

    elif choice == "7":
        bank.show_accounts()
        print("Total balance:", bank.total_balance())

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option")