# E-Commerce Order Analysis
'''..................................
Write a program to: 
• Display all products costing more than ₹1000.  
• Find the most expensive product.  
• Calculate the total order value.  
• Count products costing below ₹1000. 
........................................'''
#An online store records
orders = [ 
    ("Laptop", 55000), 
    ("Mouse", 800), 
    ("Keyboard", 1500), 
    ("Monitor", 12000), 
    ("Pen Drive", 600) 
]
#............................................
#Display all products costing more than ₹1000.
print("products costing more than ₹1000")
for item in orders:
    if item[1] > 1000:
        print(item[0],item[1])
#...............................................
#Find the most expensive product.
most_expensive = orders[0]
for item in orders:
    if item[1] > most_expensive[1]:
        most_expensive = item
print("most expensive item is ",most_expensive)
#...................................................
#Calculate the total order value
total_order = 0
for item in orders:
    total_order = total_order+item[1]
print("total order value is :", total_order)
#..................................................
#Count products costing below ₹1000.
count_product = 0
for item in orders:
    if item[1] < 1000:
        count_product= count_product+1
print("product costing below ₹1000 :",count_product)        

