PIN = "1234"
balance = 5000


def check_balance():
    print(f"\nCurrent Balance: rs.{balance}")


def deposit():
    global balance

    try:
        amount = float(input("Enter amount to deposit: rs."))

        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            balance += amount
            print(f"rs.{amount} deposited successfully.")
            print(f"New Balance: rs.{balance}")

    except ValueError:
        print("Please enter a valid amount.")


def withdraw():
    global balance

    try:
        amount = float(input("Enter amount to withdraw: rs."))

        if amount <= 0:
            print("Amount must be greater than 0.")

        elif amount > balance:
            print("Insufficient Balance.")

        else:
            balance -= amount
            print(f"rs.{amount} withdrawn successfully.")
            print(f"Remaining Balance: rs.{balance}")

    except ValueError:
        print("Please enter a valid amount.")


def menu():

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using our ATM.")
            break

        else:
            print("Invalid choice. Try again.")


def login():

    attempts = 3

    while attempts > 0:

        entered_pin = input("Enter 4-digit PIN: ")

        if entered_pin == PIN:
            print("\nLogin Successful!")
            menu()
            return

        attempts -= 1

        if attempts > 0:
            print(f"Incorrect PIN. Attempts left: {attempts}")

    print("\nYour account has been locked.")


login()
