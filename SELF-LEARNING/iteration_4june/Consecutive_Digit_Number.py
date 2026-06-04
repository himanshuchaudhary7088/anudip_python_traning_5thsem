# Program to check whether a number is a Consecutive Digit Number

# Accept a number from the user
num = int(input("Enter a number: "))

# Validate input
if num <= 0:
    print("Invalid Input! Please enter a positive number.")

else:
    # Store original number
    temp = num

    # Assume the number is consecutive
    consecutive = True

    # Check consecutive digits from right to left
    while temp > 9:

        # Get the last digit
        digit1 = temp % 10

        # Get the previous digit
        digit2 = (temp // 10) % 10

        # Check whether current digit is exactly
        # 1 greater than the previous digit
        if digit1 - digit2 != 1:
            consecutive = False
            break

        # Remove the last digit
        temp = temp // 10

    # Display result
    if consecutive:
        print("Consecutive Number")
    else:
        print("Not a Consecutive Number")