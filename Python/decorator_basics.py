def decor(function):
    def wrapper(*args, **kwargs):
        res = function(*args, **kwargs)
        print('some action')
        return res
    return wrapper

def foo():
    print('hello')

f = decor(foo)
f()

@decor
def bar():
    print('bye')

bar()


@decor
def dummy(a,b,c):
    return a+b+c

d = dummy(1,2,3)
print(d)