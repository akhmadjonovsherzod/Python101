from typing import Dict

def combine_dicts(*args:Dict[str, int]) -> Dict[str, int]:
    my_dict = {}

    for dict in args:
        for i in dict:
            if not i in my_dict:
                my_dict[i] = dict[i]
            else:
                my_dict[i] += dict[i]

    return my_dict