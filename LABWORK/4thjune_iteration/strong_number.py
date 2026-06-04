# Program to check whether a number is a Strong Number

# Accept a number from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Variable to store the sum of factorials of digits
sum = 0

# Extract each digit of the number
while num > 0:

    # Get the last digit
    digit = num % 10

    # Calculate factorial of the digit
    factorial = 1

    for i in range(1, digit + 1):
        factorial = factorial * i

    # Add factorial to the sum
    sum = sum + factorial

    # Remove the last digit
    num = num // 10

# Check whether the number is Strong or not
if sum == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is Not a Strong Number")