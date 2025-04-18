"""Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*"""
def print_pattern(n):
    for i in range(1, n + 1):
        print('*' * (n - i + 1))


n = int(input("Enter the number of lines to print: "))
print_pattern(n)

