def my_range(n):
    print('Starting')
    i = 0
    while i < n:
        yield i
        i += 1
    return 0

g = my_range(10)
for i in g:
    print(i)
    
for i in g:
    print(g)