from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    my_lst = []

    for i in sequence:

        if isinstance(i, (tuple, list)):

            my_lst.extend(linear_seq(i))
        else:
            my_lst.append(i)

    return my_lst