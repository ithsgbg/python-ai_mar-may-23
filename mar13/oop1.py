class Person:
    def __init__(self, name, age=10):
        self._name = name
        self.age = age
        
    @property
    def name(self):
        """
        Getter
        """
        return self._name
    
    @name.setter
    def name(self, value):
        """
        Setter
        """
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value
    
    
    
p1 = Person('Alice', 32)    
p2 = Person('Bob', 45)
p1.name = 99
print(p1.name) 
