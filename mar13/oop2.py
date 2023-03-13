def person_class(name, age):
    # Private member varaibles
    private_name = name
    private_age = age
    
    def init():
        pass
    
    def get_name():
        return private_name
    
    def set_name(new_name):
        nonlocal private_name
        private_name = new_name

    def get_age():
        return private_age
    
    def set_age(new_age):
        nonlocal private_age
        private_age = new_age
        
    init.get_name = get_name
    init.set_name = set_name
    init.get_age = get_age
    init.set_age = set_age
    
    return init
    
    
p1 = person_class('Alice', 32)
print(p1.get_name(), p1.get_age())
p1.set_name('Lisa')
print(p1.get_name(), p1.get_age())
p2 = person_class('Bob', 55)
print(p2.get_name(), p2.get_age())
print(p1.get_name(), p1.get_age())
    