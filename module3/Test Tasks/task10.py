from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:

    collector = []
    if not len(lst) == 0:
        for i in range(len(lst) - 1):
            the_t = lst[i], lst[i+1]
            collector.append(the_t)
        return collector
    return []