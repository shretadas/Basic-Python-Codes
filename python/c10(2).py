#Write a class “Calculator” capable of finding square, cube and square root of a number.
import math

class Calculator:
    def __init__(self, number):
        self.number = number
    
    def square(self):
        return self.number ** 2
    
    def cube(self):
        return self.number ** 3
    
    def square_root(self):
        return math.sqrt(self.number)

number = float(input("Enter a number: "))

calc = Calculator(number)


print(f"Square of {calc.number} is: {calc.square()}")
print(f"Cube of {calc.number} is: {calc.cube()}")
print(f"Square root of {calc.number} is: {calc.square_root():.2f}")
