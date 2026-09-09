from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:

    result = []

    start = 0

    for ind in indexes:
        if ind < 0 or len(s) < ind:
            continue

        result.append(s[start:ind])

        start = ind

    result.append(s[start:])

    return result


print(split_by_index("no luck", [2, 42]))