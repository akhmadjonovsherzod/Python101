from typing import Union, List

ListType = List[Union[int, str]]


def get_fizzbuzz_list(n: int) -> ListType:
    fizzy_ls = []
    for i in range(1, n+1):
        if not (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0  and i % 5 == 0):
            fizzy_ls.append(i)
        else:
            if i % 3 == 0 and i % 5 == 0:
                fizzy_ls.append("FizzBuzz")
            elif i % 3 == 0 and not i % 5 == 0:
                fizzy_ls.append("Fizz")
            elif i % 5 == 0 and not i % 3 == 0:
                fizzy_ls.append("Buzz")
    return fizzy_ls