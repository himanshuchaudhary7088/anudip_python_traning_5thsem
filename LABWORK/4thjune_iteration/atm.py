# ATM Simulation System

# Initial account balance
balance = 10000

# Display menu repeatedly until user chooses Exit
while True:

    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    # Accept user's choice
    choice = int(input("Enter your choice: "))

    # Check Balance
    if choice == 1:
        print("Current Balance = Rs.", balance)

    # Deposit Money
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount Deposited Successfully")
        print("Updated Balance = Rs.", balance)

    # Withdraw Money
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))

        # Check whether sufficient balance is available
        if amount <= balance:
            balance = balance - amount
            print("Amount Withdrawn Successfully")
            print("Remaining Balance = Rs.", balance)
        else:
            print("Insufficient Balance")

    # Exit
    elif choice == 4:
        print("Thank You for Using ATM")
        break

    # Invalid Choice
    else:
        print("Invalid Choice. Please Try Again.")