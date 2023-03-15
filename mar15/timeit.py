import time

def time_it(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f'Call to function {f.__name__} took {end-start} seconds')
        return result
    return wrapper