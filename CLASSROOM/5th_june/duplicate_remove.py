# WAP to create a list of 20 numbers given by user.
# Ask the user to input any other number.
# Remove all duplicate entries of this number from the list.

numbers = []

# Input 20 numbers
for i in range(20):
    num = int(input("Enter number : "))
    numbers.append(num)

print("\nOriginal List:")
print(numbers)

# Number whose duplicates are to be removed
target = int(input("\nEnter a number: "))
#finding frequency of given number
freq = numbers.count(target)
if freq == 0:
    print("element not found ")
elif freq==1:
    print("no duplicates found")
else:
    #reversing the list
    numbers.reverse()
    for i in range(1,freq):
        numbers.remove(target)
    numbers.reverse()
    print("after removing duplicates")
    print(numbers)    
