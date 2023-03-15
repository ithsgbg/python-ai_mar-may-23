values = [23, 4, 23, 1, 3, 56, 7]

def mapper(a):
    return a + 2

result = list(map(lambda x: x + 2, values))
print(result)