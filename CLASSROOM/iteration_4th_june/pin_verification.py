#An ATM machine requires the user to enter the correct PIN to access their account. The valid PIN is 1234. 
#Write a program that repeatedly asks the user to enter a PIN until the correct PIN is entered.
#correct pin
pin = 1234
#enter  the pin
entered_pin = int(input("Enter the four digit PIN: "))
#check the pin
while entered_pin != pin:
    print("Wrong PIN")
    entered_pin = int(input("Enter the four digit PIN again: "))
#pin verified
print("----******----")
print("PIN Verified")