#

def my_deco(function_to_decorate):

    def wrapper_func():
        print("Initializing...")

        function_to_decorate()

        print("Closing...")
    return wrapper_func

def stable_f():
    print("Normal")

dcrtd = my_deco(stable_f)

dcrtd()

#2nd method

@my_deco #this is called decorator syntax
def stable_f_2():
    print("This is the second normal")

stable_f_2()

#it is possible to pass the args into the decorator function

def decor(org_func):

    def wrapper(arg1, arg2):

        print("Input arguments:", arg1, arg2)

        org_func(arg1, arg2)
    return wrapper


@decor
def stbl_func(first, last):

    print("Firstname:", first, "Lastname:", last)

stbl_func("S", "H")

#directly transferring the args into deco func

def decorator_maker(decorator_arg1, decorator_arg2):
    print('I create decorators. I got the following arguments:', decorator_arg1, decorator_arg2)

    def decorator_function(func):
        print('I am a decorator. I got a function:', func)

        def wrapper(function_arg1, function_arg2):
            print(
                'I am a wrapper around the origin function.\nAnd I have access to all
            arguments: \n'
            f'\t- and decorator: {decorator_arg1} {decorator_arg2}\n'
            f'\t- and functions: {function_arg1} {function_arg2}\n'
            )
            return func(function_arg1, function_arg2)

        return wrapper

    return decorator_function