from functools import wraps


def decorator_apply(function):
    """
    Create a decorator that applies a function to the result
    of the decorated function.

    :param function: Function that accepts one positional argument.
    :return: A decorator.
    """

    def decorator(org_func):
        """
        Decorate a function and apply the given function to its result.

        :param org_func: Function that will be decorated.
        :return: Wrapper function.
        """

        @wraps(org_func)
        def wrapper(*args, **kwargs):
            """
            Call the original function and apply the given function
            to its result.
            """

            result = org_func(*args, **kwargs)

            return function(result)

        return wrapper

    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int):
    """
    Return the given user ID.

    :param num: User ID.
    :return: User ID.
    """

    return num