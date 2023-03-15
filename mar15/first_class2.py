class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def __str__(self):
            return f'{self.name}, is {self.age} years old and has email address {self.email}'   
    
def person_compare(p):
    return p.name
    
    
p1 = Person('Bob', 27, 'bob@email.com')
p2 = Person('Carl', 19, 'carl@email.com')
p3 = Person('Alice', 29, 'alice@email.com')

persons = [p1, p2, p3]
# sorted_persons = sorted(persons, key=person_compare)
sorted_persons = sorted(persons, key=lambda p: p.age, reverse=True)
for person in sorted_persons:
    print(person)