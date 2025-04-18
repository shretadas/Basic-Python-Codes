#Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?
class MyClass:
    a = 1  

obj = MyClass()
print(f"Class attribute 'a': {MyClass.a}")
print(f"Object attribute 'a': {obj.a}")

obj.a = 0

print(f"Class attribute 'a': {MyClass.a}")
print(f"Object attribute 'a': {obj.a}")
"""Yes, setting object.a = 0 directly on an instance of a class does not change the class attribute a. """
