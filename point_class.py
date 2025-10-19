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


def main():
    """Main driver function to demonstrate Point class functionality"""
    print("=== Point Class Demonstration ===\n")
    
    # Create points
    print("1. Creating points:")
    p1 = Point(3, 4)
    p2 = Point(7, 10)
    p3 = Point()  # Default constructor
    
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p3 = {p3}")
    print()
    
    # Test translation
    print("2. Testing translation:")
    print(f"Before translation: p1 = {p1}")
    p1.translate(2, 3)
    print(f"After translating p1 by (2, 3): p1 = {p1}")
    print()
    
    # Test distance from origin
    print("3. Testing distance from origin:")
    print(f"Distance of {p1} from origin: {p1.odistance():.2f}")
    print(f"Distance of {p2} from origin: {p2.odistance():.2f}")
    print(f"Distance of {p3} from origin: {p3.odistance():.2f}")
    print()
    
    # Test addition
    print("4. Testing point addition:")
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    result = p1 + p2
    print(f"p1 + p2 = {result}")
    print()
    
    # Test error handling
    print("5. Testing error handling:")
    try:
        p1 + 5  # This should raise TypeError
    except TypeError as e:
        print(f"Error caught: {e}")


if __name__ == "__main__":
    main()