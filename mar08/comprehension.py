values = [1, 2, 3, 4, 5, 6]

new_values = []
for value in values:
    if value % 2 == 0:
        new_values.append(value*2)
    else:
        new_values.append(0)
    
print(new_values)


new_values = tuple([value*2 for value in values])
print(new_values)