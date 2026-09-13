from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    sqrd_dict = {}

    for i in range(1, num + 1):
        sqrd_dict[i] = i**2

    return sqrd_dict
