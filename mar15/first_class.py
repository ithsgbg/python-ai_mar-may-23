def func(a, b):
    return a + b

def func2(a, b):
    return a * b

def func3(a, b):
    return f'I got {a} and {b} as arguments'

def my_func(a, b, calc_func):
    return calc_func(a, b)


result = my_func(10, 3, func3)
print(result)


