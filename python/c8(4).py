#Write a recursive function to calculate the sum of first n natural numbers.
def sum_of_natural_numbers(n):
    return n if n == 1 else n + sum_of_natural_numbers(n - 1)


n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    
    result = sum_of_natural_numbers(n)
    print(f"The sum of first {n} natural numbers is: {result}")
