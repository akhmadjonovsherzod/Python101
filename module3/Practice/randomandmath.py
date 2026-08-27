import math
import random

a = 60

converted_to_radians = math.radians(60) #converts the angle to radians
converted_to_cos = math.cos(converted_to_radians) #converts the radians to cosine
converted_to_sin = math.sin(converted_to_radians) #converts the radians to sine

print(converted_to_radians)
print(converted_to_cos)
print(converted_to_sin)

x = 5
y = 6

clhypot = math.hypot(x, y) #calculates the euclidian distance between 2 numbers

print("Euclidian distance for ", x, "and", y, "is", clhypot)

print(math.isnan(x)) #checks if x is NOT a number, if FALSE, then it is a number

