#Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce


numbers = [23, 45, 17, 88, 52, 39, 71, 92]


max_number = reduce(lambda x, y: x if x > y else y, numbers)

print("Maximum number in the list:", max_number)
