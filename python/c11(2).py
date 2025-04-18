#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self, name):
        self.name = name

class Pets(Animals):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

class Dog(Pets):
    def bark(self):
        return f"{self.name} says: Woof!"


my_dog = Dog("Buddy", "Alice")
print(my_dog.bark())
