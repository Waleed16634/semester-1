# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?
# the .pop removes and returns the last item on the list

# What features of Python does it rely on?
# The while loop will keep going if there is anything in the list and if the list becomes empty then the while loop will return FALSE therefore stopping the loop
