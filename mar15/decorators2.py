import time
from functools import wraps

def repeat(n, delay):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = f(*args, **kwargs)
                time.sleep(delay)
            return result
        return wrapper
    return decorator
    

@repeat(3, 2)
def say_hi(name):
    print(f'Hi {name}')
    
    
@repeat(5, 1)
def greet(greeting, name):
    print(f'{greeting}, {name}')
  
  
print(say_hi.__name__)  
print(greet.__name__)  
# say_hi('Anna')
# greet('Yo', 'Bob')