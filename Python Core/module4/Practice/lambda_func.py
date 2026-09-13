# lambda arg1, arg2, ...: <statement>

my_rect_calc = lambda x, y: 2*(x+y)

print(my_rect_calc(3, 4))

# sorting using lambda and without lambda

#without

def filter_function(pair_item):
    return pair_item[1]

pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort(key=filter_function)
print(pairs)

#with

pairs.sort(key=lambda pair_item: pair_item[1])

print(pairs)

# map()

sqrbls = [1, 2, 3, 4, 5]

square_all = map(lambda num: num ** 2, sqrbls)

print(square_all)

print(list(square_all))

# filter()

nums = [48, 6, 9, 21, 1, 35, 16, 12, 0, -1]
print(list(filter(lambda num: num % 2 == 0, nums)))

print(list(filter(None, nums)))

#functools.reduce

from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])) #works like (((1+2)+3)+4)+5
