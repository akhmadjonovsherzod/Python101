from typing import Union


def divide(str_with_ints: str) -> Union[float, str]:
    div = str_with_ints.split()

    try:
        a = int(div[0])
        b = int(div[1])
        result = a / b
    except ValueError as e:
        return f"Error code: {e}"
    except ZeroDivisionError as z:
        return f"Error code: {z}"
    except IndexError as i:
        return f"Error code: {i}"

    return result

    # raise NotImplementedError('Implement me!')


print(divide("1"))