#Add a static method in problem 2, to greet the user with hello.
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
    @staticmethod
    def greet_user():
        print("Hello! Welcome to the Calculator program.")

    

number = float(input("Enter a number: "))

calc = Calculator(number)
Calculator.greet_user()


print(f"Square of {calc.number} is: {calc.square()}")
print(f"Cube of {calc.number} is: {calc.cube()}")
print(f"Square root of {calc.number} is: {calc.square_root():.2f}")

