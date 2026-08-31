from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    cvrt_str = str(num)
    my_list = list(cvrt_str)
    new_ls = []
    for i in my_list:
        el = int(i)
        new_ls.append(el)

    my_tuple = tuple(new_ls)
    return my_tuple