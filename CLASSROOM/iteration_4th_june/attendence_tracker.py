# A teacher is recording attendence of a class of strength 30 every time he needss to check every student is present or absent display how many students are present and absent
# Program to record attendance of 30 students

roll_no = 1
present = 0
absent = 0

while roll_no <= 30:
    print("Roll No =", roll_no)
    status = input("Present(P) or Absent(A): ")

    if status == "P":
        present = present + 1
    else:
        absent = absent + 1

    roll_no = roll_no + 1

print("Present Students =", present)
print("Absent Students =", absent)