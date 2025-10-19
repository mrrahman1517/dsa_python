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
    
p = Point(3, 4)
q = Point(7, 10)

print(p + q)