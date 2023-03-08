def my_func(name:str, age:int=30):
    print(f'Hello {name}, you are {age}')
    print('Hello ' + name + ' ' + str(age))
    print('Bye')
    return f'Hello {name}, you are {age}', age + 10
    
    
def other_func(a, b, *args, name, **kwargs):
    print('a =', a)
    print('b =', b)
    for arg in args:
        print(arg)
    print('name =', name)
    for k, v in kwargs.items():
        print(k, v)
    

other_func(1, 2, 3, 4, 5, name='John', age=23)
other_func(1, 2, name='Pete')

