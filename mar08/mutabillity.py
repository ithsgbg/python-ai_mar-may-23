from copy import deepcopy

# x = 1000
# y = 1000

# print(id(x))
# print(id(y))

# y += 1
# print(id(x))
# print(id(y))
# -5 to 256

# name1 = 'Alice'
# name2 = 'Alice'

# print(id(name1))
# print(id(name2))
# name2 += 'x'
# print(id(name1))
# print(id(name2))

values1 = [1, 2, 3, 4]
values2 = deepcopy(values1)

print(id(values1))
print(id(values2))
values1.append(99)
print(values1)
print(values2)
