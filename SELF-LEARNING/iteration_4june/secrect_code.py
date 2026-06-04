# Program to check whether a secret code is valid

# Accept secret code from user
code = input("Enter a 6-digit secret code: ")

# Validate length of the code
if len(code) != 6:
    print("Invalid Code")

else:

    # Initialize variables to store sums
    first_sum = 0
    last_sum = 0

    # Initialize loop counter
    i = 0

    # Calculate sum of first 3 digits
    while i < 3:
        first_sum = first_sum + int(code[i])
        i = i + 1

    # Calculate sum of last 3 digits
    while i < 6:
        last_sum = last_sum + int(code[i])
        i = i + 1

    # Compare both sums
    if first_sum == last_sum:
        print("Valid Code")
    else:
        print("Invalid Code")