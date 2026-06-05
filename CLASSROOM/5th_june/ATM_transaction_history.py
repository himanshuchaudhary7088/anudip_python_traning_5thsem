#ATM transaction history 
#atm history 
transactions = [5000, -2000, 3000, -1000, -500, 7000]
#withdrawl list
withdrawl = []
#deposite list 
deposite = []
#initialize the curent balance
current_balacne=0
total_deposite=0
total_withdrawl=0
#largest deposite and largest withdrawl
largest_deposite = 0
largest_withdrawl = 0
#check the transactions
for i in transactions:
    current_balacne = current_balacne+i
    if i < 0 :
        withdrawl.append(i)
    else:
        deposite.append(i)
        #print withdrawl and deposite lists
print("total withdrawl list:",withdrawl)
print("total deposite list :",deposite)
#check the withdrawl
for j in withdrawl:
    total_withdrawl = total_withdrawl+j
    if j < largest_withdrawl:
        largest_withdrawl = j
print("total withdrawl :",total_withdrawl)
print("largest withdrawl :",largest_withdrawl)

#check the deposite 
for k in deposite:
    total_deposite = total_deposite+k
    if k > largest_deposite:
        largest_deposite = k
print("total deposite:", total_deposite)
print("largest deposite :", largest_deposite)





