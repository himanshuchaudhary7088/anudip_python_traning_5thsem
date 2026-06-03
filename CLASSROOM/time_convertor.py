#program to convert time into corresponding hours,minutes and second
#input of time in second
second = int(input("enter the time in second"))
#check second is negative:
if(second < 0):
    exit("time cannot be negative")
#..............................................................\
print("------------------------------------------------")
hour = 0
minute = 0
#converting number of seconds into hours
if(second >= 3600):
    hour = second//3600
    second = second % 3600
#..............................................................
#convert into minutes
if(second >= 60):
    minute = second // 60
    second = second % 60

#print time 
print(hour,"hours",minute,"minute",second,"seconds")