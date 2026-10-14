# Worksheet 1.2: Task 1 Solution
import sys
Grade = input("Please enter a grade from 0-100: ")

if Grade.isdecimal() and int(Grade) in range(101):
    Grade = int(Grade)
    print("The grade you have entered is valid")

    if Grade >= 70:
        print(Grade, "is a distinction")
    elif Grade >= 40:
        print(Grade, "is a pass")
    else:
        print(Grade, "is a fail")

else:
    print("Error: Grade must be an integer between 0 an 100")
