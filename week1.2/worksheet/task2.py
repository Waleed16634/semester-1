# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

Numbers = read_numbers()

if len(Numbers) == 0:
    sys.exit("Error: no numbers provided")

Numbers.sort()
n = len(Numbers)

if n % 2 == 1:
    median = Numbers[n//2]
else:
    median = (Numbers[n//2-1]+Numbers[n//2])/2


print("Minimum =", min(Numbers))
print("Maximum =", max(Numbers))
print("Mean =", sum(Numbers)/n)
print("Median =", median)
