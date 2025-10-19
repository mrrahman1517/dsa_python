class Point:
    def __init__(self, a = 0, b = 0):
        self.x = a
        self.y = b 

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay 

    def odistance(self):
        import math 
        d = math.sqrt(self.x * self.x + self.y * self.y)
        return(d)
    
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("add only works for Point type")
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
q = Point(7, 10)

print(p + q)