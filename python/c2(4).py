#Write a python program to find an average of two numbers entered by the user.
def average():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    average=(num1+num2)/2
    print(f"the average of {num1} and {num2}: {average}")
average()
