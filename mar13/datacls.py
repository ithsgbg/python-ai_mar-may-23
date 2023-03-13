from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def swap(self):
        self.x, self.y = self.y, self.x
    
p = Point(10, 5)
p2 = Point(10, 5)

print(p)

p.swap()
print(p)