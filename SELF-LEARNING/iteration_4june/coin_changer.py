# Program to find minimum number of notes

# Accept amount
amount = int(input("Enter the amount: "))

# Validate input
if amount <= 0:
    print("Invalid Amount")

else:

    # Calculate 500 notes
    notes_500 = amount // 500
    amount = amount % 500

    # Calculate 200 notes
    notes_200 = amount // 200
    amount = amount % 200

    # Calculate 100 notes
    notes_100 = amount // 100
    amount = amount % 100

    # Calculate 50 notes
    notes_50 = amount // 50
    amount = amount % 50

    # Calculate 20 notes
    notes_20 = amount // 20
    amount = amount % 20

    # Calculate 10 notes
    notes_10 = amount // 10
    amount = amount % 10

    # Display notes used
    if notes_500 > 0:
        print("500 x", notes_500)

    if notes_200 > 0:
        print("200 x", notes_200)

    if notes_100 > 0:
        print("100 x", notes_100)

    if notes_50 > 0:
        print("50 x", notes_50)

    if notes_20 > 0:
        print("20 x", notes_20)

    if notes_10 > 0:
        print("10 x", notes_10)

    # Check remaining amount
    if amount > 0:
        print("Remaining Amount =", amount)