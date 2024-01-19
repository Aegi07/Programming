# example 1 - logging

def logged(function):
    
    def wrapper(*args, **kwargs):
        val = function(*args, **kwargs)
        with open('Python/logs/logfile.txt', 'a+') as f:
            fname = function.__name__
            f.write(f'{fname} returned value {val}\n')

        return val
    
    return wrapper

@logged
def add(x, y):
    return x + y

# print(add(10,20))

# example 2 - timing
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        val = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f'{fname} took {after-before} seconds to execute')
        return val
    return wrapper

@timed
def myfunc(x):
    result = 1
    for i in range(1, x):
        result += i
    return result


print(myfunc(100_000))
print(myfunc(100_000_000))