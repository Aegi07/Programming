# taking arguments as part of python run command
import sys

def foo(*args, **kwargs):
    res1 = []
    res2 = {}
    for arg in args:
        res1.append(arg)
    
    for k, v in kwargs.items():
        res2[k] = v
    return res1, res2

if __name__ == '__main__':
    print(sys.argv) # result is a list, starting from file name, then arg1, arg2, etc...
    res1, res2 = foo(sys.argv[1], key2=sys.argv[2], key3=sys.argv[3])
    print(res1)
    print(res2)

    # python3 argparse_basics.py arg1 arg2 arg3