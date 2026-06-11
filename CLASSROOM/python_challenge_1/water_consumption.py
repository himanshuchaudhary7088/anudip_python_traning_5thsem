'''Problem Statement 
Monthly water consumption (in litres) of households is recorded below. 
Sample Data 
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
} 
Tasks 
1. Display houses consuming more than 3000 litres.  
2. Find the highest and lowest consumers.  
3. Calculate total water consumption.  
4. Categorize houses:  
o Low (<2000 litres)  
o Medium (2000–3500 litres)  
o High (>3500 litres)  
5. Count households eligible for conservation awareness programs (>2500 litres). '''
# --------------------------------------
# Water Consumption Analysis    
# Sample Data
water_usage = { 
    "House101": 1800, 
    "House102": 2200, 
    "House103": 3500, 
    "House104": 2800, 
    "House105": 1600, 
    "House106": 4100, 
    "House107": 2400, 
    "House108": 3900, 
    "House109": 1500, 
    "House110": 4500 
}
# Function to display houses consuming more than 3000 litres
print("Houses consuming more than 3000 litres:")
for house, usage in water_usage.items():
    if usage > 3000:
        print(house)
# Function to find the highest and lowest consumers
highest_consumer = water_usage["House101"]
lowest_consumer = water_usage["House101"]
for usage in water_usage.values():
    if usage > highest_consumer:
        highest_consumer = usage
    if usage < lowest_consumer:
        lowest_consumer = usage
print("\nHighest Consumer: ", highest_consumer, "litres")
print("Lowest Consumer: ", lowest_consumer, "litres")   
# Function to calculate total water consumption
total_consumption = 0
for usage in water_usage.values():
    total_consumption += usage
print("\nTotal Water Consumption: ", total_consumption, "litres")
# Function to categorize houses
print("\nHouse Categories:")
for house, usage in water_usage.items():
 if usage < 0:
    print("enter a valid value")
    break
 else:  
     if usage < 2000:
        category = "Low"
     elif 2000 <= usage <= 3500:
        category = "Medium"
     else:
        category = "High"
     print(house, ":", category)
# Function to count households eligible for conservation awareness programs (>2500 litres)
conservation_count = 0
for usage in water_usage.values():
    if usage > 2500:
        conservation_count += 1
print("\nNumber of households eligible for conservation awareness programs: ", conservation_count)
