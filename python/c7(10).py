#Write a program to print multiplication table of n using for loops in reversed order.
number=int(input("enter the number:"))
print(f"multiplication of {number}:")
for i in range(10,0,-1):
    print(f"{number}x{i}={number*i}")