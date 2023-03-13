class Person:
    __slots__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'

        
p1 = Person('Alice', 29)
p2 = Person('Bob', 45)

p1.email = 'alice@email.com'

