#Override the __len__() method on vector of problem 5 to display the dimension of the vector.
class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

    def __len__(self):
        return len(self.components)


v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)  
print(v1 * v2)  
print(len(v1))  
