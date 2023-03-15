def make_power_func(power):
    
    def power_func(n):
        return n**power
    
    return power_func


square = make_power_func(2)
cube = make_power_func(3)
result = square(4)
print(result)
result = square(5)
print(result)
result = square(6)
print(result)

result = cube(4)
print(result)
result = cube(5)
print(result)
result = cube(6)
print(result)

