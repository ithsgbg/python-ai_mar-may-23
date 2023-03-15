values = [23, 4, 23, 1, 3, 56, 7]

def filter_func(a):
    return a > 3


result = list(filter(lambda x: x > 3, values))
print(result)