from typing import List

def common(l1: List, l2: List) -> List:
    ret = set()
    for element1 in l1:
        for element2 in l2:
            if element1 == element2:
                ret.add(element1)
    return sorted(list(ret))