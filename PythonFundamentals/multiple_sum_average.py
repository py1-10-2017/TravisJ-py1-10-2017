# Multiples - Part 1
# Prints all the odd numbers from 1 to 1000 using a for loop
for oddNum in range(1, 1000):
    if oddNum % 2 != 0:
        print oddNum


# Multiples - Part 2
# Prints all the multiples of 5 from 5 to 1000000 using a for loop
for multFive in range(5, 1000000):
    if multFive % 5 == 0:
        print multFive

# Sum List
# This is a program that adds all values in a list
a = [1, 2, 5, 10, 255, 3]

print sum(a)

# Average List
# This program prints the average of the list
average = sum(a) / len(a)

print average
