#Write a program to filter a list of numbers which are divisible by 5.
numbers = [10, 23, 45, 68, 75, 82, 90, 105, 120]

divisible_by_5 = [num for num in numbers if num % 5 == 0]
print("Numbers divisible by 5:", divisible_by_5)


