from mar15.timeit import time_it
import time

@time_it
def my_func(a, b):
    print('starting')
    time.sleep(a)
    print('I am awake')
    time.sleep(b)
    print('I am done')
    

#my_func = time_it(my_func)

#print(my_func.__name__)
my_func(1, 2)