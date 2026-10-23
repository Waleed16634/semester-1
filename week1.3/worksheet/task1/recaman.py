# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input

# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]

for k in range(1, L):
    next_number = sequence[k - 1] - k

    if next_number > 0 and next_number not in sequence:
        sequence.append(next_number)
    else:
        next_number = sequence[k - 1] + k
        sequence.append(next_number)

# You may wish to use further output for testing purposes while you develop your code

# this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence

[print(item) for item in sequence]
