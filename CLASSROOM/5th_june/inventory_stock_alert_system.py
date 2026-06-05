#An inventory manager stores stock quantities as:
#stock = [25, 5, 0, 12, 3, 18, 0, 30]
#Write a program to:
#1. Display products that are out of stock.
#2. Display products that need restocking (quantity less than 10).
#3. Count available products.
#4. Create a new list containing only products with stock greater than or equal to 15. 

stock = [25, 5, 0, 12, 3, 18, 0, 30]

# products need restocking
restock_required = []

# products having more than or equal to 15 quantity
healthy_stock = []

# count available products
available_products = 0

# display the products out of stock
out_of_stock = stock.count(0)
print("out of stock products :", out_of_stock)

for i in stock:

    # count available products
    if i > 0:
        available_products += 1

    # restock required
    if i < 10:
        restock_required.append(i)

    # item that have more than or equal to 15 quantities
    if i >= 15:
        healthy_stock.append(i)

print("restock required :", restock_required)
print("healthy stock :", healthy_stock)
print("available products :", available_products)