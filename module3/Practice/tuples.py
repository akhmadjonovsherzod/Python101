# tuples are immutable

the_c = ("red", "green", "blue")

print(type(the_c))

# without parantheses

the_c_2 = "red", "green", "blue"

print(type(the_c_2))

# to create a tuple with one element, we need to put ","

this_is_tuple = (1,)

print(type(this_is_tuple))

# unpacking operator *

the_unpacker = (1, 2, 3)

print(the_unpacker)
print(*the_unpacker)

# swapping the values

a, b = 1, 2
print(a, b)

b, a = a, b
print(a, b)
