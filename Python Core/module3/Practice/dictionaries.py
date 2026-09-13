#to create
#1st
my_dictionary = {
    "name": "Sherzodbek",
    "age": 22,
    "occupation": "student"
}

print(my_dictionary)

#2nd
my_dictionary_2 = dict([("name", "Sherzodbek"), ("age", 22), ("occupation", "student")])

print(my_dictionary)

#access

print(my_dictionary["name"])

#update

my_dictionary["age"] = 33

print(my_dictionary)

#remove

del my_dictionary["occupation"]

print(my_dictionary)

#it is iterable and supports loop

for pair in my_dictionary.items():
    print(pair)

for key, value in my_dictionary.items():
    print((key, value))

#membership check

if "name" in my_dictionary and my_dictionary["name"]:
    print(my_dictionary["name"])

#The get() method takes a key as a parameter and returns the value by this key. The method doesn't raise an error if the key doesn't exist:

print(my_dictionary.get("preferences", "there is noting"))

#The items() method returns the iterable object dict_items where each element is a tuple of the form (key, value):
for pair in my_dictionary.items():
    print(pair)

#The keys() method returns a dict_keys object which contains keys from a dictionary and the values() method returns dict_values object with values of a dictionary. Both these objects are sequence objects:

for key in my_dictionary.keys():
    print(key)

#The update() method takes another dictionary or some collection of key-value pairs as an argument and updates all matching pairs in the original dictionary and adds key-value pairs for keys that don’t exist in the original dictionary:

blank_d = {
    "name": "",
    "age": 0,
    "is_registered": False,
    "rate": 0,
    "total_score": 0,
    "linked_ids": []
}

my_dictionary.update(blank_d)
print(my_dictionary)