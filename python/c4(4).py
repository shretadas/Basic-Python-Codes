#Write a program to sum a list with 4 numbers.
def sum_list():
    num = []
    for i in range(4):
        number = int(input(f"Enter number {i + 1}: "))
        num.append(number)
    
    total_sum = sum(num)
    
    print("Numbers entered:", num)
    print("Sum of the numbers:", total_sum)

sum_list()
