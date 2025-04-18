"""Create a class ‘Employee’ and add salary and increment properties to it.
Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter which changes the value of increment based on the salary."""
class Employee:
    def __init__(self, salary, increment):
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100

emp = Employee(50000, 10)
print(f"Salary After Increment: {emp.salaryAfterIncrement}")

emp.salaryAfterIncrement = 60000
print(f"New Increment: {emp.increment}%")

