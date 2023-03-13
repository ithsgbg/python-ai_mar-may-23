class Person:
    def __new__(cls, name):
        print(f'Creating an object from class {cls.__name__} with the name {name}')
        return super().__new__(cls)
    
    def __init__(self, name):
        print(f'Initializing the person object {name}')
        self.name = name
        self.age = None
        
        
p1 = Person('Lisa')