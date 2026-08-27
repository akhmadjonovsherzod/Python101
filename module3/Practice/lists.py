# lists can include any data type inside

my_first_list = ["Hello", 33, True, "everybody!"]

print(type(my_first_list))

# change by index

my_first_list[2] = False

print(my_first_list)

# add new item

my_first_list.append("New item")

print(my_first_list)

# lists are iterable

some_numbers = [1, 3, 5, 9, 11, 16, 28, 44.7, 90.6, 5334]
for i in some_numbers[::2]:
    print(i)

# list manipulations

some_numbers = [11, 5, 16, 28, 5334, 44.7, 90.6, 1, 3, 9]
some_numbers.sort()
print(some_numbers)

print(len(some_numbers))

#extend() - adds a new item from another iterable object, like another list

some_list = [1, 2, 3]
some_str = "abc"
some_list.extend(some_str)
print(some_list)

x = 1
some_list = [1, 2, 3, 2, 1, 1]
print(some_list.count(x))

# pop() removes the item from the list, given by index, by default removes the last item

my_stack = [1, 2, 3]
my_stack.append(4)
my_stack.append(5)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

# list comprehension

n = int(input("Enter a number: "))

even_numbers = [i for i in range(1, n) if not i % 2]

print(even_numbers)