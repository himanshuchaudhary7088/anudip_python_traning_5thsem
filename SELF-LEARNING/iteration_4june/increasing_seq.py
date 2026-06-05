# Program to find longest continuous increasing sequence

# Accept number of elements
n = int(input("Enter total numbers: "))

# Validate input
if n <= 0:
    print("Invalid Input")

else:

    # Take first number
    prev = int(input("Enter number 1: "))

    # Initialize counters
    current_length = 1
    longest_length = 1

    i = 2

    # Loop for remaining numbers
    while i <= n:

        num = int(input("Enter number: "))

        # Check increasing sequence
        if num > prev:
            current_length = current_length + 1
        else:
            if current_length > longest_length:
                longest_length = current_length
            current_length = 1

        prev = num
        i = i + 1

    # Final check
    if current_length > longest_length:
        longest_length = current_length

    print("Longest Sequence Length =", longest_length)