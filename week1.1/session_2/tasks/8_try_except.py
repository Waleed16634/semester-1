#this loop continues the program until an error occurs

try:
    num1 = int(input("Enter your number"))
    num2 = int(input("Enter your number"))
    result = num1+num2
    print("the first number + the second number =", result)
except:
    print("Please enter only numbers")