#Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80
def compare_number():
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    if a>b:
        print(f"{a} is greater than{b}")
    else:
        print(f"{a} is greater than {b}")
        
compare_number()