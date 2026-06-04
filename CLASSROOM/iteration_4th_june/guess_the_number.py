#A game has selected a secret number 7. The player must keep guessing the number until the correct guess is made. 
#Write a program that repeatedly asks the user to guess the number and displays a success message when the correct number is entered.
# Program to guess the secret number

secret_number = 7

# Take first guess from the user
guess = int(input("Guess the number: "))

# Keep asking until the correct number is guessed
while guess != secret_number:
    print("Wrong Guess. Try Again.")
    guess = int(input("Guess the number: "))

# Display success message
print("Congratulations! You guessed the correct number.")