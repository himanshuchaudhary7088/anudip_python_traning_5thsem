# Program to calculate electricity bill

# Accept units consumed
units = int(input("Enter electricity units consumed: "))

# Validate input
if units < 0:
    print("Invalid Input! Units cannot be negative.")
else:

    # Calculate bill according to slabs
    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    # Apply surcharge if bill exceeds ₹5000
    if bill > 5000:
        surcharge = bill * 0.10
        bill = bill + surcharge

    # Display final bill
    print("Final Payable Amount = ₹", bill)