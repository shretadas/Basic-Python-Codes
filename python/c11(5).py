#Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        return sum(a * b for a, b in zip(self.components, other.components))

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)  
print(v1 * v2)  
