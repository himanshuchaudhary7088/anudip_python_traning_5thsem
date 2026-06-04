# Program to check whether a number is a Mirror Number

# Accept number
num = int(input("Enter a number: "))

# Validate input
if num < 0:
    print("Invalid Input")

else:

    # Count digits
    temp = num
    digits = 0

    while temp > 0:
        digits = digits + 1
        temp = temp // 10

    # Check whether number has even digits
    if digits % 2 != 0:
        print("Not a Mirror Number")

    else:

        # Find divisor = 10^(digits/2)
        divisor = 1
        i = 1

        while i <= digits // 2:
            divisor = divisor * 10
            i = i + 1

        # Extract left and right halves
        left_half = num // divisor
        right_half = num % divisor

        # Compare halves
        if left_half == right_half:
            print("Mirror Number")
        else:
            print("Not a Mirror Number")