''' Shopping Cart Application (Intermediate) 
Problem Statement: 
Create a Product class containing product name, quantity, and price per unit. 
Implement methods to: 
• Calculate total price.  
• Update quantity.  
• Display product details. '''
#program to implement a shopping cart application using a class
class Product:
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
    #method to calculate total price
    def total_price(self):
        print("Total Price: Rs.", self.quantity * self.price_per_unit)
    #method to update quantity
    def update_quantity(self, new_quantity):
        if new_quantity < 0:
            exit("Quantity cannot be negative.")
        else:    
             self.quantity = new_quantity
             print("Updated Quantity:", self.quantity)
    #method to display product details
    def display_details(self):
        print("Product Name:", self.name)
        print("Quantity:", self.quantity)
        print("Price per Unit: Rs.", self.price_per_unit)
#---------------------------------------------------
# ask the user to enter product details
name = input("Enter product name: ")
#to validate product name input    
if name.isspace():
    exit("Product name cannot be empty.")
quantity = int(input("Enter quantity: "))
#to validate quantity input 
if quantity < 0:
    exit("Quantity cannot be negative.")        
price_per_unit = float(input("Enter price per unit: "))
#to validate price per unit input        
if price_per_unit < 0:
    exit("Price per unit cannot be negative.")
new_quantity = int(input("enter the udated quantity"))  
#vaalidate the new quantity
if new_quantity<0:
    exit("quantity cannot be negative") 
# create a Product object with the entered details
product = Product(name, quantity, price_per_unit)
print("-----------product details-----------")
# calculate and display total price
product.total_price()
print("--------------------------------------------------------")
# update quantity
product.update_quantity(new_quantity)

# display updated details
product.display_details()
product.total_price()