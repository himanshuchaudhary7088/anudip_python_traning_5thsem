'''Problem Statement 
The prices of products added to a shopping cart are stored below. 
Sample Data 
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999] 
Tasks 
1. Calculate the total cart value.  
2. Find the most expensive and cheapest products.  
3. Count products eligible for premium shipping (price > ₹1000).  
4. Generate a discount list (products above ₹1500).  
5. Calculate the average product price.  '''
# --------------------------------------
# Shopping Cart Analysis
# Sample Data
cart = [1500, 899, 450, 2500, 799, 1200, 300, 650, 1800, 999]
# Function to calculate the total cart value
total_cart_value = 0
for price in cart:
    total_cart_value += price
print("Total Cart Value: ₹", total_cart_value)
# Function to find the most expensive and cheapest products
most_expensive = cart[0]
cheapest = cart[0]
for price in cart:
    if price > most_expensive:
        most_expensive = price
    if price < cheapest:
        cheapest = price
print("Most Expensive Product: ₹", most_expensive)
print("Cheapest Product: ₹", cheapest)
# Function to count products eligible for premium shipping (price > ₹1000)
premium_shipping_count = 0
for price in cart:
    if price > 1000:
        premium_shipping_count += 1
print("Products Eligible for Premium Shipping: ", premium_shipping_count)
# Function to generate a discount list (products above ₹1500)
discount_list = []
for price in cart:
    if price > 1500:
        discount_list.append(price)
print("Discount List: ₹", discount_list)
# Function to calculate the average product price
average_price = total_cart_value / len(cart)
print("Average Product Price: ₹", average_price)