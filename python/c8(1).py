#Write a program using functions to find greatest of three numbers.
def find_greatest(num1,num2,num3):
    return max(num1,num2,num3)
num1=int(input("enter the first number:"))
num2=int(input("enter the seconf number:"))
num3=int(input("enter the third number:"))
greatest=find_greatest(num1,num2,num3)
print(f"the greatest of three numbers {num1},{num2},{num3}:{greatest}")
find_greatest()
