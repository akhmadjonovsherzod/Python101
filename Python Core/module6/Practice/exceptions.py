#try, except, else, finally

try:
    fh = open("files.txt", "r")
    # fh.write("This is my test file for handling the error")
except IOError:
    print("Error! Can\'t find the file")
else:
    print("success!")
    fh.close()

try:
    fh = open("filesss.txt", "w")
    fh.write("This is my test file for handling the error")
except IOError:
    print("Error! Can\'t find the file")
finally:
    fh.close()

try:
    a = int(input("Enter a number: "))
    if a <= 0:
        raise ValueError("It should be positive!")
except ValueError as ve:
    print(ve)

#creating a custom exception

class InputError(Exception):
    pass

#it can be raised in the same as other exceptions

class Exception1(Exception):
   pass

class Exception2(Exception1):
   pass

try:
   if isinstance(2, int):
       raise Exception2
except Exception1:
   print("Exception1 is caught")
except Exception2:
   print("Exception2 is caught")