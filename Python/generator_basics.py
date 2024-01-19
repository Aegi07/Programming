import sys

def gen(x):
    for i in range(x):
        yield i

def get_size(generator):
    return f"size is {sys.getsizeof(generator)}"

vals = gen(10)

## size is constant regardless of vals
print(get_size(vals))

for i in range(5):
    print(next(vals))

print(get_size(vals))

for x in vals:
    print(x)

print(get_size(vals))