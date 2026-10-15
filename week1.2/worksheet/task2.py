# Worksheet 1.2: Task 2 Solution
import statistics

Users_Numbers = input("Please enter a sequence of float values ")
Values = []
for x in Users_Numbers.split():
    try:
        Values.append(float(x))
    except ValueError:
        print("Error: please enter a valid number")
        exit()

if not Values:
    print("Error: nothing was entered")
    exit()

Minimum_Value = min(Values)
Maximum_Value = max(Values)
Mean_Value = statistics.mean(Values)
Median_Value = statistics.median(Values)

print("The Minimum Value is", Minimum_Value)
print("The Maximum Value is", Maximum_Value)
print("The Mean Value is", Mean_Value)
print("The Median Value is", Median_Value)
