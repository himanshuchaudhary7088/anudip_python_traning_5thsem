# Program to find the length of the longest continuous increasing sequence

# Accept total numbers
n = int(input("Enter the total number of numbers: "))

# Validate input
if n <= 0:
    print("Invalid Input! Count must be greater than 0.")
else:

    # Input first number
    previous = int(input("Enter number 1: "))

    # Initialize counters
    current_length = 1
    longest_length = 1

    # Accept remaining numbers
    i = 2

    while i <= n:

        num = int(input("Enter number " + str(i) + ": "))

        if num > previous:
            current_length = current_length + 1
        else:
            if current_length > longest_length:
                longest_length = current_length

            current_length = 1

        previous = num
        i = i + 1

    if current_length > longest_length:
        longest_length = current_length

    # Display result
    print("Longest Sequence Length =", longest_length)