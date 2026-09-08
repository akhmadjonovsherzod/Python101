from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    my_sum = 0

    for i in sequence:

        if isinstance(i, (list, tuple)):

            my_sum = my_sum + seq_sum(i)

        else:
            my_sum += i

    return my_sum
