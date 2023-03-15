from functools import reduce

values = [23, 14, 5, 16, 2, 19]

def my_reduce(func, iterable):
    if len(iterable) < 2:
        return iterable
    val1 = iterable[0]
    val2 = iterable[1]
    val1 = func(val1,val2)
    for i in range(2, len(iterable)):
        val2 = iterable[i]
        val1 = func(val1,val2)
    return val1

def reducer(a, b):
    return a * b

result = reduce(lambda a, b: a * b, values)
print(result)