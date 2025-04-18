#Write a program to print third, fifth and seventh element from a list using enumerate function.
elements = [10, 20, 30, 40, 50, 60, 70, 80, 90]

for index, element in enumerate(elements):
    if index in [2, 4, 6]:  # Third element is at index 2, fifth at index 4, and seventh at index 6
        print(element)
