# Worksheet 1.2: Task 1 Solution
import sys
Grade = input("Please enter a grade from 0-100: ")

if not Grade.isdecimal() or int(Grade) > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100")

Grade = int(Grade)

if Grade >= 70:
    print(Grade, "is a Distinction")
elif Grade >= 40:
    print(Grade, "is a Pass")
else:
    print(Grade, "is a Fail")
