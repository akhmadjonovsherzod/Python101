#function with return statement

def power(num_1, num_2):     # get input value
    result = num_1 ** num_2  # perform calculation
    return result         		   # provide the result

# function without return statement

def welcome_greeting(name):   # might be without input arguments
    print(f'Hello, {name}!')  	# do some actions
                          			    # no return statement

#we can assign functions to variables

def square(x):
    return x ** 2

funcable = square

print(funcable(5))

# we can pass the functions as arguments
def apply_func(func, *args):
    results = []
    for arg in args:
        results.append(func(arg))

    return results

print(apply_func(square, 25))

# we can save the functions in data structures

def cube(x):
    return x ** 3

treeple = {
    'cube': cube
}

print(treeple["cube"](6))

# returning functions

def get_func(func_name):
    func_mapper = {
        "cube": cube,
        "square": square
    }

    return func_mapper.get(func_name, None)

frizz = get_func("square")

print(frizz(6))

# positional and keyword arguments

def show_arguments(*args, **kwargs):
  print(f"args: {args}; kwargs: {kwargs}")

  