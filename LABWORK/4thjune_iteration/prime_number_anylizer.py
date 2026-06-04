# Program to check whether a number is Prime or Not Prime
# If the number is not prime, display all its factors

# Accept a number from the user
num = int(input("Enter a number: "))

# Variable to count the factors of the number
count = 0

# Find all factors of the number
for i in range(1, num + 1):

    # Check whether i is a factor of num
    if num % i == 0:
        count = count + 1

# A prime number has exactly 2 factors
if count == 2:
    print(num, "is a Prime Number")

else:
    print(num, "is Not a Prime Number")

    # Display all factors of the number
    print("Factors are:")

    for i in range(1, num + 1):

        # Check whether i is a factor
        if num % i == 0:
            print(i)