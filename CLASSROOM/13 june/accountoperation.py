#creating a class to open from various operation for a costumer account
class Account:
    #defining a constructor
    def __init__(self, name, acno, balance):
        self.__name = name
        self.__acno = acno
        self.__balance = balance
    #method to display the account details
    def display_account_details(self):
        print("Name:" ,self.__name)
        print("Number:",self.__acno)
        print("Balance:",self.__balance)
    #---------------------------------------------------
    # method to deposit money into the account
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited: Rs.", amount)
        print("Available Balance: Rs.", self.__balance)    
    #---------------------------------------------------
    # method to withdraw money from the account
    def withdraw(self, amount):    
        if (self.__balance-amount)<=1000:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Withdrawn: Rs.", amount)
            print("Available Balance: Rs.", self.__balance)
    #---------------------------------------------------
    # method to display available balance in the account
    def display_balance(self):
        print("Available Balance: Rs.", self.__balance)
    #-------------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------------
    #------------  main program -----------------------------------------             
    #ask the user to enter the account details
name = input("Enter your name: ")
#to validate name input
if name.isspace():
    exit("Name cannot be empty.")
acno = int(input("Enter your six-digit account number: "))
#to validate account number input
if acno < 100000 or acno > 999999:
    exit("Invalid account number.")
balance = float(input("Enter your initial balance: "))
#to validate balance 
if balance < 1000:
    exit("Initial balance must be at least Rs. 1000.")

# create an object of the Account class
account = Account(name, acno, balance)
#menu-driven program to perform various operations on the account
while True:
    print("\n_________account operations_________:")
    print("1. Display account details")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("4. Display available balance")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        account.display_account_details()
    elif choice == 2:
        amount = float(input("Enter the amount to deposit: "))
        #to validate deposit amount
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else: 
             account.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter the amount to withdraw: "))
        #to validate withdraw amount
        if amount <= 0:
            print("Withdraw amount must be greater than zero.")
        else:
             account.withdraw(amount)
    elif choice == 4:
        account.display_balance()
    elif choice == 5:
        print("Thank you for using our services!")
        break
    else:
        print("Invalid choice! Please try again.") 
    #-----------------------------------------------------------
    # ask the user if they want to perform another operation
    another_operation = input("Do you want to perform another operation? (y/n): ")
    if another_operation.lower() != 'y':
        print("Thank you for using our services!")
        break
    print    