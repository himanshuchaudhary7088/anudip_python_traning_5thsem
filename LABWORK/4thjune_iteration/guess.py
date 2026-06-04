# Number Guessing Game

# Secret number
secret_number = 7

# Count attempts
attempts = 0

# Take first guess
guess = int(input("Enter a number between 1 and 50: "))

while guess != secret_number:

    # Check whether the number is in range
    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50")

    # Check whether guess is high or low
    elif guess > secret_number:
        print("Too High")

    else:
        print("Too Low")

    attempts = attempts + 1

    # Take another guess
    guess = int(input("Enter a number between 1 and 50: "))

# Count the correct attempt
attempts = attempts + 1

print("Correct Guess")
print("Total Attempts =", attempts)