#Write a program to find the sum of first n natural numbers using while loop.
n=int(input("enter the number:"))
sum_numbers=0
i=1
while i<=n:
    sum_numbers +=i
    i +=1
    print(f"the sum of first n natural numbers {n}:{sum_numbers}")