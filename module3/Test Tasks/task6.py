from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str, ...]) -> List[str]:
    new_ls = []

    for i in str_list:
        if not i in new_ls:
            new_ls.append(i)
            new_ls.sort()
    return new_ls
