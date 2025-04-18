#Create a class (2-D vector) and use it to create another class representing a 3-D vector.
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
    
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

vec2d = Vector2D(1, 2)
vec3d = Vector3D(3, 4, 5)

print(vec2d)
print(vec3d)
