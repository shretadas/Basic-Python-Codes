#Write a program to print multiplication table of a given number using while loop.
number = int(input("Enter the number: "))
i = 1
print(f"Multiplication table for {number}:")
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1
