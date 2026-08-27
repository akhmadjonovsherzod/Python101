#while loop

# x = int(input("Enter 0 to stop: "))
# sum_x = 0
#
# while x !=0:
#     sum_x += x
#     x = int(input("Enter 0 to stop: "))
#
# print(sum_x)

#continue

# n = int(input("Input integer number: "))
# sum_result = 0
# x = 1
#
# while x < n:
#     x += 1
#     if x % 2:
#         continue
#     sum_result += x
#
# print(f"Sum of even numbers: {sum_result}")

#break

# x = int(input("Please enter a number: "))
# is_prime = True
# div = 2
#
# while div < x:
#     if not x % div:
#         is_prime = False
#         break
#     div += 1
#
# if is_prime:
#     print("Prime")
# else:
#     print("Not prime")

x = int(input("Please enter a number: "))
is_prime = True

for div in range(2, x):
    if not x % div:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not a prime")