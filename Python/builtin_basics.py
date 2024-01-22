# def add(x,y):
#     return x+y
# # is equivalent to... 
# f = lambda x,y: x+y
# print(add(1,2)==f(1,2))
# print(f'normal: {add.__name__}')
# print(f'lambda: {f.__name__}') # lambda is nameless

## map(), filter(), reduce()

# map(func, iterable) applies the function to every element in target iterable
nums = [i for i in range(10)]
print(f'old list: {nums}')
nums = list(map(lambda x: x*x, nums))
print(f'new list: {nums}')

# filter(condition, iterable) applies the condition (function) to every element in target iterable, return only the true elements
nums = list(filter(lambda x: x%2==0, nums))
print(f'(filtered) even list: {nums}')

# reduce(function, iterable) reduces the iterable to 1 element using the function
from functools import reduce
nums = reduce(lambda x,y: x*y, nums[1:])
print(f'reduced list: {nums}') # returns the sum of the entire list

