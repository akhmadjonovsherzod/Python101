my_set = {1, 113.5, True, "Some string"}

print(type(my_set))

#empty set

my_set_1 = {}
print(type(my_set_1))

#duplicates

my_set = set([1, 2, 3, 1, 2])
print(my_set)

#sets are iterable

for item in my_set:
    print(item)

#Hash, hash()

hash_value = hash((1, 2, 3))

print(hash_value)

#union, intersect, difference operator

s1 = {"a", "d", "h"}
s2 = {"n", "b", "c", "d"}
s3 = {"c", "d"}
union = s1 | s2 | s3 #or union = s1.union(s2, s3)
print(union)

s1 = {"a", "d", "h"}
s2 = {"n", "b", "c", "d", "a"}
s3 = {"n", "a", "d"}
my_intersection = s1 & s2 & s3 #or my_intersection = s1.intersection(s2, s3)
print(my_intersection)

s1 = {"a", "d", "h", "c", "j"}
s2 = {"n", "b", "c", "d", "a"}
s3 = {"n", "a", "d"}
my_difference = s1 - s2 - s3 #or my_difference = s1.difference(s2, s3)
print(my_difference)

#update()

#The update method changes the value of the original set to the union with the specified sets:

s1 = {"a", "b", "k"}
s2 = {"a", "d", "h"}
s3 = {"n", "b", "d"}

s1.update(s2, s3)
print(s1)

#The intersection_update and the difference_update methods work similarly, but with intersection and difference, respectively.

#adding and removing

s1 = {1, 2, 3}
s1.add("string")
s1.remove(1)

print(s1)

#clear() clears the whole set

s4 = {1, 2, 3}
s4 = s4.clear()
print(s4)