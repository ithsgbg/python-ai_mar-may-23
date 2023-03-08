def func(value=10):
    value += 1
    return value


def func2(name, names=None):
    if names is None:
        names = []
    names.append(name)
    return names


result = func()
print(result)
result = func()
print(result)

result1 = func2('Alice')
print(result1)
result2 = func2('Bob')
print(result2)
result3 = func2('Carl')
print(result3)