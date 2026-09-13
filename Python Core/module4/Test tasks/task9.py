from functools import wraps


def validate(org_func):
    """
    Decorator that validates all arguments of the function.

    All arguments must be integers between 0 and 256 inclusive.

    :param org_func: The function that will be validated.
    :return: A wrapper function that performs the validation.
    """

    @wraps(org_func)
    def wrapper(*args, **kwargs):
        """
        Check that all function arguments are valid.
        """

        # Check positional arguments
        for value in args:
            if not isinstance(value, int) or value < 0 or value > 256:
                return "Function call is not valid!"

        # Check keyword arguments
        for value in kwargs.values():
            if not isinstance(value, int) or value < 0 or value > 256:
                return "Function call is not valid!"

        # If all arguments are valid, call the original function
        return org_func(*args, **kwargs)

    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
    """
    Create a pixel using three coordinates.

    :param x: X coordinate.
    :param y: Y coordinate.
    :param z: Z coordinate.
    :return: A message indicating whether the pixel was created.
    """

    return "Pixel created!"


