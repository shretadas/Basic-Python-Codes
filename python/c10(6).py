#Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.
class MyClass:
    def __init__(harry, value):
        harry.value = value
    
    def print_value(harry):
        print(f"Value: {harry.value}")

# Creating an instance of MyClass
obj = MyClass(42)

# Calling the print_value method
obj.print_value()
"""while you can change self to another valid variable name like harry, it's best practice to use self for clarity and consistency across Python codebases."""