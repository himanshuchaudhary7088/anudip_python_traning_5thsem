# Program to check Reverse Number and Palindrome Number

# Accept a number from the user
num = int(input("Enter a number: "))

# Store the original number
original_num = num

# Variable to store the reverse number
reverse = 0

# Reverse the number
while num > 0:

    # Get the last digit
    digit = num % 10

    # Add the digit to the reverse number
    reverse = reverse * 10 + digit

    # Remove the last digit
    num = num // 10

# Display the reverse number
print("Reverse Number =", reverse)

# Check whether the number is palindrome or not
if reverse == original_num:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")