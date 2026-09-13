from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    itemz = []
    for i in lst:
        for v in i.values():
            itemz.append(v)

    itemz_set = set(itemz)

    return itemz_set
