class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    
    
p = Point(10, 5)
p2 = Point(10, 5)

print(p == p2)