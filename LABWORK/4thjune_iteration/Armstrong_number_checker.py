# Program to check whether a number is an Armstrong Number

# Accept a number from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Variable to store the sum of cubes of digits
sum = 0

# Extract each digit and calculate the sum of cubes
while num > 0:

    # Get the last digit
    digit = num % 10

    # Add the cube of the digit to sum
    sum = sum + (digit ** 3)

    # Remove the last digit
    num = num // 10

# Check whether the number is Armstrong or not
if sum == original_num:
    print(original_num, "is an Armstrong Number")
else:
    print(original_num, "is Not an Armstrong Number")