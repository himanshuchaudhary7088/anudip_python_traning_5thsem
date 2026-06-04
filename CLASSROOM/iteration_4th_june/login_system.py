#A website allows users to log in using a password. The correct password is admin123. 
#Write a program that keeps asking the user to enter the password until the correct password is provided
# Program to verify website password

# Store the correct password
password = "admin123"

# Run the loop continuously
while True:

    # Take password from user
    entered_password = input("Enter Password: ")

    # Check whether password is correct
    if entered_password == password:
        print("Login Successful")
        break   # Exit the loop

    # Password is incorrect
    else:
        print("Incorrect Password. Try Again.")